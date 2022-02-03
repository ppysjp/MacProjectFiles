set nocompatible              " be iMproved, required
filetype off                  " required

" set the runtime path to include Vundle and initialize
set rtp+=~/.vim/bundle/Vundle.vim

call vundle#begin()
" alternatively, pass a path where Vundle should install plugins
"call vundle#begin('~/some/path/here')

" let Vundle manage Vundle, required
Plugin 'wlangstroth/vim-racket'
Plugin 'paredit.vim'
Plugin 'ervandew/supertab'
Plugin 'benmills/vimux' "VimuxRunCommand
Plugin 'amdt/vim-niji'
Plugin 'VundleVim/Vundle.vim'
Plugin 'jremmen/vim-ripgrep'
Plugin 'tpope/vim-fugitive'
Plugin 'leafgarland/typescript-vim'
Plugin 'lyuts/vim-rtags'
Plugin 'kien/ctrlp.vim'
Plugin 'mbbill/undotree'
Plugin 'vim-utils/vim-man'
Plugin 'christoomey/vim-tmux-navigator'
Plugin 'morhetz/gruvbox'
Plugin 'neoclide/coc.nvim'
Plugin 'sheerun/vim-polyglot'
Plugin 'vim-airline/vim-airline'

" All of your Plugins must be added before the following line
call vundle#end()            " required


function! VimuxSlime()
 call VimuxSendText(@v)
 call VimuxSendKeys("Enter")
endfunction

"######################################################
" SCHEME MAPPINGS
"######################################################

let maplocalleader = ","
nmap <LocalLeader>rr :call VimuxRunCommand("racket -i -p neil/sicp -l xrepl")<CR>
" Exit racket
nmap <LocalLeader>e :call VimuxRunCommand("^Z")<CR>
" break racket
nmap <LocalLeader>br :call VimuxRunCommand("^C")<CR>
" Clear Racket
nmap <LocalLeader>cl :call VimuxRunCommand(",sh clear")<CR>
" Back Trace Racket
nmap <LocalLeader>bt :call VimuxRunCommand(",bt")<CR>
"Dr Racket
nmap <LocalLeader>dr :call VimuxRunCommand(",drracket")<CR>
"Racket Help 
nmap <LocalLeader>h :call VimuxRunCommand(",h")<CR>

" Select current paragraph and send it to tmux
nmap <LocalLeader>vs vip<LocalLeader>vs<CR>
"Link Vim to Nearest Tmux pane 
nmap <LocalLeader>vo :call VimuxOpenRunner()<CR>

" define a process in scheme
nmap <LocalLeader>def i(define (f x) (* x x<Esc>%b%l

" define a lambda in scheme
nmap <LocalLeader>ll i(lambda (x) (+ x x<Esc>>%b% 

" define a let in scheme
nmap <LocalLeader>let i(let ((a (+ 1 x))<Esc>%%a(<Esc>i<CR>
            \<Esc><Esc>%ib (- 1 y)))<Esc><Esc>%%a(<Esc>i<CR><Esc>%
        \i+ a b<Esc>kk

" define a if in scheme
nmap <LocalLeader>if i(if (> x 0) (+ x 1) (- x 1<Esc>bbbbb%i<CR>  <Esc>%wi<CR>
            \<Esc>lkkl

" define a cond in scheme
nmap <LocalLeader>cond i(cond ((= a 1) 1)((= b 2) 2)(else 3<Esc>%i<CR><Esc>k%wi
            \<CR><Esc>kw  

" define a and in scheme
nmap <LocalLeader>and i(and (> a 1) (< b 2<Esc>%b% 

" define a and in scheme
nmap <LocalLeader>or i(or (> a 1) (< b 2<Esc>%b% 

" define a cons in scheme
nmap <LocalLeader>cons i(cons a b<Esc>% 

" define a car in scheme
nmap <LocalLeader>car i(car x<Esc>% 

" define a cdr in scheme
nmap <LocalLeader>cdr i(cdr x<Esc>% 

" define a cdr in scheme
nmap <LocalLeader>map i(map proc sequence)<Esc>% 

" define a cdr in scheme
nmap <LocalLeader>flat i(flatmap proc seq)<Esc>% 

" define a cdr in scheme
nmap <LocalLeader>fil i(filter predicate sequence)<Esc>% 

" define a cdr in scheme
nmap <LocalLeader>acc i(accumulate op initial sequence)<Esc>% 

" define a cdr in scheme
nmap <LocalLeader>enuml i(enumerate-interval low high)<Esc>% 

" define a cdr in scheme
nmap <LocalLeader>enumt i(enumerate-tree tree)<Esc>% 

" Motion commands for scheme
nmap <LocalLeader>rem i(require racket/math<Esc>

" Motion commands for scheme
nmap <LocalLeader>ret i(require racket/trace<Esc>

" Motion commands for scheme
nmap <LocalLeader>put i(put op type item)<Esc>%

"######################################################
"######################################################
"######################################################
"######################################################
"######################################################
"######################################################
"######################################################
 
" If text is selected, save it in the v buffer and send that buffer it to tmux
vmap <LocalLeader>vs "vy :call VimuxSlime()<CR>


filetype plugin indent on    " required
" To ignore plugin indent changes, instead use:
"filetype plugin on
"
" Brief help
" :PluginList       - lists configured plugins
" :PluginInstall    - installs plugins; append `!` to update or just :PluginUpdate
" :PluginSearch foo - searches for foo; append `!` to refresh local cache
" :PluginClean      - confirms removal of unused plugins; append `!` to auto-approve removal
"
" see :h vundle for more details or wiki for FAQ
" Put your non-Plugin stuff after this line

"######################################################
" COC SETTINGS
"######################################################

function! s:check_back_space() abort
  let col = col('.') - 1
  return !col || getline('.')[col - 1]  =~ '\s'
endfunction


fun! GoCoc()
    inoremap <buffer> <silent><expr> <TAB>
                \ pumvisible() ? "\<C-n>" :
                \ <SID>check_back_space() ? "\<TAB>" :
            \ coc#refresh()

inoremap <buffer><expr><S-TAB> pumvisible() ? "\<C-p>" : "\<C-h>"
inoremap <buffer> <silent><expr> <C-space> coc#refresh()

nmap <buffer> <silent> gd <Plug>(coc-definition)
nmap <buffer> <silent> gy <Plug>(coc-type-definition)
nmap <buffer> <silent> gi <Plug>(coc-implementation)
nmap <buffer> <silent> gr <Plug>(coc-references)
nnoremap <buffer> <leader>cr :CocRestart
endfun

autocmd FileType cpp,python,cxx,h,hpp,c,c++ :call GoCoc()
autocmd filetype lisp,scheme,art setlocal equalprg=scmindent.rkt

set background=dark
colorscheme gruvbox
"
"######################################################
syntax on
"######################################################
set autoread
set nocompatible              " required
set tabstop=4 softtabstop=4
set shiftwidth=4
set expandtab
set smartindent
set relativenumber 
set number
set nowrap " means that along line will just keep going of the page
set smartcase " Case sensitive searching until you put in a Capital
set noswapfile
set nobackup
set incsearch
set colorcolumn=80
set splitright
set splitbelow
highlight ColorColumn ctermbg=0 guibg=lightgrey

let mapleader = " "


"######################################################
" DIRECTORY BROWSER SETTINGS 
"######################################################

" guard for distributions lacking the 'persistent_undo' feature.
if has('persistent_undo')
    " define a path to store persistent undo files.
    let target_path = expand('~/.config/vim-persisted-undo/')
    " create the directory and any parent directories
    " if the location does not exist.
    if !isdirectory(target_path)
        call system('mkdir -p ' . target_path)
    endif
    " point Vim to the defined undo directory.
    let &undodir = target_path
    " finally, enable undo persistence.
    set undofile
endif

"
"######################################################
" DIRECTORY BROWSER SETTINGS
"######################################################
let g:netrw_browse_split=2
let g:netrw_banner = 0
let g:netrw_winsize = 25
let g:ctrlp_use_caching = 0
" touch .ctrlp will create a marker to 
let g:ctrlp_root_markers = ['.ctrlp'] 
"######################################################
" LEADER KEY REMAPPINGS
"######################################################
nnoremap <leader>w :w!<CR>
nnoremap <leader>e :q!<CR>
nnoremap <leader>h :wincmd h<CR>
nnoremap <leader>j :wincmd j<CR>
nnoremap <leader>k :wincmd k<CR>
nnoremap <leader>l :wincmd l<CR>
nnoremap <leader>rg :sp<CR>:Rg 
nnoremap <leader>mv :vp<CR>:e $MYVIMRC<CR>
nnoremap <leader>u :UndotreeShow<CR>
nnoremap <leader>uh :UndotreeHide<CR>
nnoremap <leader>m :vs <bar> :e $MYVIMRC<CR>
nnoremap <leader>hh :vert bo help<CR>
nnoremap <leader>b :buffers<CR>:buffer<Space>
"
"nnoremap <leader>hj :vert bo help jedi-vim<CR>
"nnoremap <leader>hn :vert bo help netrw<CR>
"nnoremap <leader>pv :wincmd v <bar> :Ex <bar> :vertical resize 30<CR> "nnoremap <leader>ps :Rg<SPACE>
nnoremap <silent> <leader>+ :vertical resize +5<CR>

"######################################################
" INSERT MODE REMAPPINGS
"######################################################
inoremap jk <Esc>

" Motion commands for scheme
nmap <LocalLeader>bo %%a(<Esc>i<CR><Esc>%i 


 
" If text is selected, save it in the v buffer and send that buffer it to tmux
vmap <LocalLeader>vs "vy :call VimuxSlime()<CR>


filetype plugin indent on    " required
" To ignore plugin indent changes, instead use:
"filetype plugin on
"
" Brief help
" :PluginList       - lists configured plugins
" :PluginInstall    - installs plugins; append `!` to update or just :PluginUpdate
" :PluginSearch foo - searches for foo; append `!` to refresh local cache
" :PluginClean      - confirms removal of unused plugins; append `!` to auto-approve removal
"
" see :h vundle for more details or wiki for FAQ
" Put your non-Plugin stuff after this line

"######################################################
" COC SETTINGS
"######################################################

function! s:check_back_space() abort
  let col = col('.') - 1
  return !col || getline('.')[col - 1]  =~ '\s'
endfunction


fun! GoCoc()
    inoremap <buffer> <silent><expr> <TAB>
                \ pumvisible() ? "\<C-n>" :
                \ <SID>check_back_space() ? "\<TAB>" :
            \ coc#refresh()

inoremap <buffer><expr><S-TAB> pumvisible() ? "\<C-p>" : "\<C-h>"
inoremap <buffer> <silent><expr> <C-space> coc#refresh()

nmap <buffer> <silent> gd <Plug>(coc-definition)
nmap <buffer> <silent> gy <Plug>(coc-type-definition)
nmap <buffer> <silent> gi <Plug>(coc-implementation)
nmap <buffer> <silent> gr <Plug>(coc-references)
nnoremap <buffer> <leader>cr :CocRestart
endfun

autocmd FileType cpp,python,cxx,h,hpp,c,c++ :call GoCoc()
autocmd filetype lisp,scheme,art setlocal equalprg=scmindent.rkt

set background=dark
colorscheme gruvbox
"
"######################################################
syntax on
"######################################################
set nocompatible              " required
set tabstop=4 softtabstop=4
set shiftwidth=4
set expandtab
set smartindent
set relativenumber 
set number
set nowrap " means that along line will just keep going of the page
set smartcase " Case sensitive searching until you put in a Capital
set noswapfile
set nobackup
set undodir=~/.vim/undodir
set undofile
set incsearch
set colorcolumn=80
set splitright
set splitbelow
highlight ColorColumn ctermbg=0 guibg=lightgrey

let mapleader = " "
"
"######################################################
" DIRECTORY BROWSER SETTINGS
"######################################################
let g:netrw_browse_split=2
let g:netrw_banner = 0
let g:netrw_winsize = 25
let g:ctrlp_use_caching = 0
" touch .ctrlp will create a marker to 
let g:ctrlp_root_markers = ['.ctrlp'] 
"######################################################
" LEADER KEY REMAPPINGS
"######################################################
nnoremap <leader>w :w!<CR>
nnoremap <leader>e :q!<CR>
nnoremap <leader>h :wincmd h<CR>
nnoremap <leader>j :wincmd j<CR>
nnoremap <leader>k :wincmd k<CR>
nnoremap <leader>l :wincmd l<CR>
nnoremap <leader>mv :e $MYVIMRC<CR>
nnoremap <leader>u :UndotreeShow<CR>
nnoremap <leader>uh :UndotreeHide<CR>
nnoremap <leader>m :vs <bar> :e $MYVIMRC<CR>
nnoremap <leader>hh :vert bo help<CR>
nnoremap <leader>b :buffers<CR>:buffer<Space>
"
"nnoremap <leader>hj :vert bo help jedi-vim<CR>
"nnoremap <leader>hn :vert bo help netrw<CR>
"nnoremap <leader>pv :wincmd v <bar> :Ex <bar> :vertical resize 30<CR> "nnoremap <leader>ps :Rg<SPACE>
nnoremap <silent> <leader>+ :vertical resize +5<CR>

"######################################################
" INSERT MODE REMAPPINGS
"######################################################
inoremap jk <Esc>
