%define	name	yodl
%define version 3.00.0

Summary:	Your Own Document Language
Name:		yodl
Version:	4.02.01
Release:	1
License:	GPLv3
Group:		Text tools
URL:		http://yodl.sourceforge.net
Source0:		https://gitlab.com/fbb-git/yodl/-/archive/%{version}/%{name}-%{version}.tar.bz2
BuildRequires:	bison, flex, diffutils, groff-for-man, libtool, netpbm, python, texinfo, icmake
BuildRequires:	texlive-latex-bin texlive-ntgclass texlive-epsf texlive-ec texlive-cm-super
BuildRequires:	texlive-texconfig ghostscript
BuildRequires:	texlive

%description
Yodl is a package that implements a pre-document language and tools to
process it. The idea of Yodl is that you write up a document in a
pre-language, then use the tools (e. g. yodl2html) to convert it to some
final document language. Current converters are for HTML, ms, man, LaTeX
SGML and texinfo, plus a poor-man's text converter. Main document types are
"article", "report", "book" and "manpage". The Yodl document language is
designed to be easy to use and extensible.

%prep
%setup -q

%build
%setup_compile_flags
./build programs
./build man
./build manual
./build macros

%install
./build install programs %{buildroot}
./build install man %{buildroot}
./build install manual %{buildroot}
./build install macros %{buildroot}
mv -f %{buildroot}%{_docdir}/yodl-doc %{buildroot}%{_docdir}/%{name}

%files
%doc README.txt README.3.00.0
%{_bindir}/yodl*
%{_mandir}/man*/yodl*
%{_datadir}/%{name}/*.yo
%{_datadir}/%{name}/chartables/*.tables.yo
%{_datadir}/%{name}/xml/*.xml
%{_datadir}/%{name}/xlatin1.tex
