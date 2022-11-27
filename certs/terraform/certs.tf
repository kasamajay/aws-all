terraform {
  # required_version = "value"
  required_providers {
    aws = {
      source = "hashicorp/aws"
      version = "4.41.0"
    }
  }
}

provider "aws" {
  region = "eu-west-2"
}


locals {
  domainName = "studydevops.co.uk"
}

data "aws_route53_zone" "main" {
  name = local.domainName
}

resource "aws_acm_certificate" "cert" {
  domain_name       = local.domainName
  validation_method = "DNS"
}

resource "aws_route53_record" "example" {
  for_each = {
    for dvo in aws_acm_certificate.cert.domain_validation_options : dvo.domain_name => {
      name   = dvo.resource_record_name
      record = dvo.resource_record_value
      type   = dvo.resource_record_type
    }
  }

  allow_overwrite = true
  name            = each.value.name
  records         = [each.value.record]
  ttl             = 60
  type            = each.value.type
  zone_id         = data.aws_route53_zone.main.id
}
