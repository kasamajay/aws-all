import pprint
import sys
import boto3
import string
import random
import time
import logging

acm_client = None
r53_client = None
domainName = 'studydevops.co.uk'
hostedZoneId = None
logging.basicConfig(level=logging.INFO)

def create_aws_clients():
    logging.info(f'--- start create_aws_clients ---')
    global acm_client 
    acm_client = boto3.client('acm')
    global r53_client
    r53_client = boto3.client('route53')
    logging.info(f'--- end   create_aws_clients ---')

def get_hosted_zone_id(domainname):
    global hostedZoneId
    logging.info(f'--- start get_hosted_zone_id fn  {domainname}---')
    
    response = r53_client.list_hosted_zones_by_name(
        DNSName=domainname
    )
    #pprint.pprint(response)
    if len(response['HostedZones']) > 0:
        hostedZoneId = response['HostedZones'][0]['Id'].rsplit('/', 1)[-1]
    else:
        pass
    logging.info(f'--- end   get_hosted_zone_id fn ---')



def generate_random_string():
    logging.info(f'--- start generate_random_string fn  ---')
    characters = string.ascii_letters + string.digits #+ string.punctuation
    str = ''.join(random.choice(characters) for i in range(8))
    logging.info(f'--- end   generate_random_string fn  ---')
    return str


def create_acm_pub_cert(dn_name):
    domain_name = dn_name
    # sub_alt_names = ['mytest.studydevops.co.uk', 'mymytest.studydevops.co.uk']
    validation_method= 'DNS'
    idem_token = generate_random_string()
    logging.info('idem token ' + idem_token)
    
    response = acm_client.request_certificate(
        DomainName=domain_name,
        ValidationMethod=validation_method,
        #SubjectAlternativeNames=sub_alt_names,
        IdempotencyToken=idem_token,
        Options={
            'CertificateTransparencyLoggingPreference': 'DISABLED'
        },
        Tags=[
            {
                'Key': 'env',
                'Value': 'test'
            },
        ],
        KeyAlgorithm='RSA_2048'
    )
    # pprint.pprint(response['CertificateArn'])
    return response['CertificateArn']
    

def print_args():
    logging.info(f"Args count: {len(sys.argv)}")
    for i, arg in enumerate(sys.argv):
        logging.info(f"sys.argv[{i}] == {arg}")
    

def delete_all_certs():
    logging.info(f'---- start delete_all_certs ----')
    arns = list_certs()
    for arn in arns:
        print(f'deleting the cert {arn}')
        response = acm_client.delete_certificate(
            CertificateArn=arn
        )
    logging.info(f'---- end   delete_all_certs ----')    

def list_certs():
    logging.info(f'---- start list_certs ----')
    response = acm_client.list_certificates()
    #print(type(response))
    
    for cert in response['CertificateSummaryList']:
        logging.info(cert['CertificateArn'])
    arns = [cert['CertificateArn'] for cert in response['CertificateSummaryList']]
    
    logging.info(f'---- end   list_certs ----')
    return arns


    # pprint.pprint(response)

def help():
    print('Syntax to use the program')
    print('python3 certs.py <command>')
    print('''Valid commands are 
        list-certs 
        delete-certs 
        create-cert''')

def help_create_cert():
    print('Syntax to use the program')
    print('python3 certs.py create-cert <domain-name>')
    print('''e.g domains are 
        game.studydevops.co.uk 
        www.studydevops.co.uk
        api.studydevops.co.uk''')

def help_describe_cert():
    print('Syntax to use the program')
    print('python3 certs.py describe-cert <cert-arn>')
    print('''e.g cert-arn are 
        arn:aws:acm:eu-west-2:502168573434:certificate/da18f485-def8-4ff7-a51d-d7c17b8e752d 
        ''')

def describe_cert(arn):
    logging.info(f'received arn {arn}')
    response = acm_client.describe_certificate(
        CertificateArn=arn
    )
    logging.info(pprint.pformat(response['Certificate']['DomainValidationOptions']))
    return response['Certificate']['DomainValidationOptions']
    #insert_records_for_domain_validation(response['Certificate']['DomainValidationOptions'])

def insert_records_for_domain_validation(validationDetails):
    logging.info(f'---- start insert_records_for_domain_validation ----')
    logging.info(pprint.pformat(validationDetails)) 
    logging.info(hostedZoneId)
    for record in validationDetails:
        print(f'name { record["ResourceRecord"]["Name"] }')
        print(f'value { record["ResourceRecord"]["Value"] }')
        print(f'type { record["ResourceRecord"]["Type"] }')
    # Z03003623QD2MJ9R4TGNO
    r53_client.change_resource_record_sets(
        HostedZoneId=hostedZoneId,
        ChangeBatch={
            'Comment': 'akk',
            'Changes': [
                {
                    'Action': 'CREATE',
                    'ResourceRecordSet': {
                        'Name': record["ResourceRecord"]["Name"],
                        'Type': record["ResourceRecord"]["Type"],
                        'ResourceRecords': [
                            {
                                'Value': record["ResourceRecord"]["Value"]
                            }
                        ],
                        'TTL': 60
                    }
                }
            ]
        }
    )


def wait_for_cert_validation(arn):
    logging.info(f'---- start wait_for_cert_validation ----')
    waiter = acm_client.get_waiter('certificate_validated')
    waiter.wait(
        CertificateArn=arn,
        WaiterConfig={
            'Delay': 123,
            'MaxAttempts': 123
        }
    )
    logging.info(f'---- end   wait_for_cert_validation ----')


def delete_all_records_in_hosted_zone():
    logging.info(f'---- start delete_all_records_in_hosted_zone ----')
    if hostedZoneId != None:
        print(f'hostedZoneId {hostedZoneId}')
        response = r53_client.list_resource_record_sets (
            HostedZoneId=hostedZoneId
        )
        cname_records = [cname_record for cname_record in response['ResourceRecordSets'] if cname_record['Type'] == 'CNAME']
        logging.info(pprint.pformat(cname_records)) 

        for cname_record in cname_records:
            logging.info(pprint.pformat(cname_record))
            logging.info(cname_record["Name"])
            logging.info(cname_record["Type"])
            r53_client.change_resource_record_sets(
                HostedZoneId=hostedZoneId,
                ChangeBatch={
                    'Changes': [
                        {
                            'Action': 'DELETE',
                            'ResourceRecordSet': cname_record
                        }
                    ]
                }
            )
    logging.info(f'---- end   delete_all_records_in_hosted_zone ----')

def delete_hosted_zone():
    logging.info(f'---- start delete_hosted_zone ----')
    if hostedZoneId != None:
        response = r53_client.delete_hosted_zone(
            Id=hostedZoneId
        )
    else:
        logging.info('Nothing to delete')
    logging.info(f'---- end   delete_hosted_zone ----')

def create_hosted_zone():
    logging.info(f'---- start create_hosted_zone ----')
    response = r53_client.create_hosted_zone(
        Name=domainName,
        CallerReference=generate_random_string(),
    )
    logging.info(pprint.pformat(response))
    logging.info(f'---- end   create_hosted_zone ----')

def cleanup():
    logging.info(f'---- start cleanup ----')
    # delete certs
    delete_all_certs()
    # delete records in hosted zone
    delete_all_records_in_hosted_zone()
    # delete hosted zone
    # delete_hosted_zone()
    logging.info(f'---- end   cleanup ----')

def setup():
    get_hosted_zone_id(domainName)
    if hostedZoneId == None:
        create_hosted_zone()

if __name__ == '__main__':
    print_args()
    if len(sys.argv) < 2:
        help()
    else:
        create_aws_clients()
        get_hosted_zone_id(domainName)
        match sys.argv[1]:
            case 'list-certs':
                logging.info('list-certs')
                list_certs()
            case 'delete-certs':
                logging.info('delete-certs')
                delete_all_certs()
            case 'create-cert':
                logging.info('create-certs')
                if len(sys.argv) < 3:
                    help_create_cert()
                else:
                    arn = create_acm_pub_cert(sys.argv[2])
                    # describe
                    time.sleep(5)
                    validationDetails = describe_cert(arn)
                    # create record in hz
                    insert_records_for_domain_validation(validationDetails)
                    wait_for_cert_validation(arn)
            case 'describe-cert':
                logging.info('describe-cert')
                if len(sys.argv) < 3:
                    help_describe_cert()
                else:
                    arn = describe_cert(sys.argv[2])
            case 'get-hosted-zone-id':
                logging.info('get-hosted-zone-id')
                get_hosted_zone_id(sys.argv[2])
            case 'delete-all-records-in-hz':
                logging.info('delete-all-records-in-hz')
                delete_all_records_in_hosted_zone()
            case 'setup':
                logging.info('setup')
                setup()    
            case 'cleanup':
                logging.info('cleanup')
                cleanup()
            case _:
                help()
