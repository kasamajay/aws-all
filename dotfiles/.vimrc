" No compatibility with old Vi is needed
set nocompatible
filetype off

set rtp+=~/.vim/bundle/Vundle.vim
call vundle#begin()
Plugin 'VundleVim/Vundle.vim'
call vundle#end()

" Activates filetype detection
filetype plugin indent on

" Activates syntax highlighting among other things
syntax on

set relativenumber
highlight LineNr ctermfg=green  

" Smart search
set ignorecase
set smartcase

"highlight search
set hlsearch

" Get rid of the newline character (\n) in the last line. Some applications don't like that character.
set noendofline binary

" Don't ident when pasting from clipboard 
set paste

" Highlight cursor position with an horizontal line.
set cursorline

" Show command in the status bar
set showcmd

" Highlight corresponding parenthesis
set showmatch

" Activate incremental search
set incsearch

" Hide buffers when not used
set hidden

" Set background color
" set background=dark

" Set file enconding to utf-8
set encoding=utf8
set fileencoding=utf-8

" Mettre 4 espaces pour l’indentation. On utilise soit la tabulation (tabstop) soit « >> » (shiftwidth).
set tabstop=3
set shiftwidth=3

" 80, le nombre maximal de caractères par ligne.
" set textwidth=80

" Ne pas couper un mot pour aller à la ligne.
set linebreak

" Avoid having swap files in my current dir, it's not good for git. Don't forget to create these folders. 
set backupdir=~/.vim/backup//
set directory=~/.vim/swap//
set undodir=~/.vim/undo//

"This unsets the "last search pattern" register by hitting return
nnoremap <CR> :noh<CR><CR>

" leave insert mode quickly
if ! has('gui_running')
	set ttimeoutlen=10
	augroup FastEscape
		autocmd!
		au InsertEnter * set timeoutlen=0
		au InsertLeave * set timeoutlen=1000
	augroup END
endif

" == Installing the asciidoc.vim file
" https://github.com/dagwieers/asciidoc-vim

" json highligther
autocmd BufNewFile,BufRead *.json set ft=javascript

" This is the Vundle package, which can be found on GitHub.
" For GitHub repos, you specify plugins using the
" 'user/repository' format
Plugin 'gmarik/vundle'

" We could also add repositories with a ".git" extension
Plugin 'scrooloose/nerdtree.git'

" To get plugins from Vim Scripts, you can reference the plugin
" by name as it appears on the site
Plugin 'Buffergator'

"CtrlP
Plugin 'kien/ctrlp.vim'

" Airline thene
Plugin 'vim-airline/vim-airline'
Plugin 'vim-airline/vim-airline-themes'

" Yaml plugin
Plugin 'avakhov/vim-yaml'

"Ag search utility
Plugin 'rking/ag.vim'

" Plugin for comments
Plugin 'tomtom/tcomment_vim'

" Docker plugin
Plugin 'ekalinin/Dockerfile.vim'


" Go plugin
Plugin 'fatih/vim-go'

" Now we can turn our filetype functionality back on

" All of your Plugins must be added before the following line
" call vundle#end()            " required

filetype plugin indent on

autocmd VimEnter * NERDTree
autocmd VimEnter * wincmd p
autocmd BufEnter * NERDTreeMirror

let mapleader = ","                                                                                                     " prefix
let maplocalleader = "\\"                                                                       " eeee
function! NumberToggle()
	if(&relativenumber == 1)
		set norelativenumber
		set number
		highlight LineNr ctermfg=yellow 
	else
		set nonumber
		set relativenumber
		highlight LineNr ctermfg=green  
	endif
endfunc

nnoremap <silent><leader>n :call NumberToggle() <cr>


function! NoNumber()
	set nonumber
	set norelativenumber
endfunc

nnoremap <silent><leader>fn :call NoNumber() <cr>

" Use The Silver Searcher https://github.com/ggreer/the_silver_searcher
if executable('ag')
	" Use Ag over Grep
	set grepprg=ag\ --nogroup\ --nocolor

	" Use ag in CtrlP for listing files. Lightning fast and respects .gitignore
	let g:ctrlp_user_command = 'ag %s -l --nocolor --hidden -g ""'

	" ag is fast enough that CtrlP doesn't need to cache
	let g:ctrlp_use_caching = 0
endif

nnoremap <leader>ev :vsplit $MYVIMRC<cr>                " Edit
nnoremap <leader>sv :source $MYVIMRC<cr>                " Load

" Disable arrow keys
noremap <Up> <Nop>
noremap <Down> <Nop>
noremap <Left> <Nop>
noremap <Right> <Nop>

" hjkl movment in insert mode via Alt key modifieh
inoremap j <C-O>gj
inoremap k <C-O>gk
inoremap h <C-O>h
inoremap l <C-O>l

" Ctrl-S to save in insert mode
inoremap <C-S> <Esc>:w<CR>a  
" inoremap <silent> <C-S> <C-O>:update<CR>
" inoremap <C-S> <C-O>:w<CR>

"To see what your terminal is sending when you press a key, switch to insert mode, press Ctrl+V, then the key

" Remap j and k movments in normal mode 
nnoremap j gj  
nnoremap k gk 

"Alt-J et Alt-K pour déplacer la ligne courante en mode normal
nmap j mz:m+<CR>'z
nmap k mz:m-2<CR>'z

"Alt-J et Alt-K pour déplacer un block de lignes en mode Visual
vmap j :m'>+<CR>'<my'>mzgv'yo'z
vmap k :m'<-2<CR>'<my'>mzgv'yo'z 

map  <C-l> :tabn<CR>
map  <C-h> :tabp<CR>
map  <C-n> :tabnew<CR>
map  <C-q> :tabclose<CR>

" Enable/Disable spell checking ... 
nnoremap ss :setlocal spell!

" Spell checking shortcurt
nnoremap <leader>sn ]s
nnoremap <leader>sp [s
nnoremap <leader>sa zg
nnoremap <leader>sz z=

" Save readonly file
command! Sudow w !sudo tee % >/dev/null


" CtrlP
" http://kien.github.io/ctrlp.vim/#installation
let g:ctrlp_map = '<c-p>'
let g:ctrlp_cmd = 'CtrlP'

let g:ctrlp_working_path_mode = 'ra'

""""""""""""""""""""""""""""""
" airline
""""""""""""""""""""""""""""""
set laststatus=2
set t_Co=256 " See PR https://github.com/vim-airline/vim-airline/pull/112
let g:airline_powerline_fonts = 1
" let g:airline_theme             = 'powerlineish'
" let g:airline_enable_branch     = 1
" let g:airline_enable_syntastic  = 1
