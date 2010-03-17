%define	name	yodl
%define version 1.31.18
%define url	ftp://ftp.lilypond.org/pub/yodl/development/

Summary:	Yet oneOther Document Language
Name:		%{name}
Version:	%{version}
Release:	%mkrel 15
License:	GPL
Group:		Text tools
URL:		http://www.xs4all.nl/~jantien/yodl
Source:		%{url}/%{name}-%{version}.tar.bz2
BuildRoot:	%{_tmppath}/%{name}-%{version}
Prefix:		%{_prefix}
Patch:		yodl-1.31.18-htmldocs.patch.bz2
Patch1:		yodl-1.31.18-compile-fix-ia64.patch.bz2
BuildRequires:	bison, flex, diffutils, groff-for-man, libtool, netpbm, python, texinfo

%description
Yodl is a package that implements a pre-document language and tools to
process it. The idea of Yodl is that you write up a document in a
pre-language, then use the tools (eg. yodl2html) to convert it to some
final document language. Current converters are for HTML, ms, man, LaTeX
SGML and texinfo, plus a poor-man's text converter. Main document types are
"article", "report", "book" and "manpage". The Yodl document language is
designed to be easy to use and extensible.

%prep
%setup -q
%patch -p1
%patch1 -p1

%build
%configure --enable-optimise --datadir=%{_datadir}/%{name}
%make
make htmldoc

%install
if [ -d $RPM_BUILD_ROOT ]; then rm -rf $RPM_BUILD_ROOT; fi
mkdir -p $RPM_BUILD_ROOT%{prefix}
%makeinstall datadir=$RPM_BUILD_ROOT%{_datadir}/%{name}
(find ./htmldocs-rpm/Documentation -size 0 | xargs rm -f)

%clean
if [ -d $RPM_BUILD_ROOT ]; then rm -rf $RPM_BUILD_ROOT; fi

%files
%defattr(-,root,root)
#
%doc *.txt ANNOUNCE-1.22 COPYING ChangeLog-1.22 TODO
%doc htmldocs-rpm/*
#
%_bindir/striproff
%_bindir/yodl
%_bindir/yodl2dvi
%_bindir/yodl2html
%_bindir/yodl2html-post
%_bindir/yodl2latex
%_bindir/yodl2less
%_bindir/yodl2man
%_bindir/yodl2man-post
%_bindir/yodl2manless
%_bindir/yodl2ms
%_bindir/yodl2ms-post
%_bindir/yodl2msless
%_bindir/yodl2msps
%_bindir/yodl2sgml
%_bindir/yodl2tely
%_bindir/yodl2tely-post
%_bindir/yodl2tex
%_bindir/yodl2texinfo
%_bindir/yodl2texinfo-post
%_bindir/yodl2txt
%_bindir/yodl2txt-post
%_bindir/yodl2whatever
%_bindir/yodlfixlabels
#
%_mandir/man1/striproff.1*
%_mandir/man1/yodl.1*
%_mandir/man1/yodlconverters.1*
%_mandir/man7/yodlmacros.7*
%_mandir/man7/yodlmanpage.7*
#
%dir %_datadir/yodl
%_datadir/yodl/*.yo
%_datadir/yodl/xlatin1.tex
#
%dir %_datadir/yodl/chartables
%_datadir/yodl/chartables/*.yo
