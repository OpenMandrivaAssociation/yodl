%define _disable_lto 1
%define _disable_ld_as_needed 1

%bcond_with docs

Summary:	Your Own Document Language
Name:		yodl
Version:	4.03.03
Release:	1
License:	GPLv3
Group:		Text tools
URL:		http://yodl.sourceforge.net
Source0:	https://gitlab.com/fbb-git/yodl/-/archive/%{version}/%{name}-%{version}.tar.bz2
BuildRequires:	icmake >= 9.02.02
BuildRequires:	stdc++-static-devel
BuildRequires:	bison
BuildRequires:	flex
BuildRequires:	diffutils
BuildRequires:	groff-for-man
BuildRequires:	libtool
BuildRequires:	netpbm
BuildRequires:	python
%if %{with docs}
BuildRequires:	texinfo
BuildRequires:	texlive-latex-bin
BuildRequires:	texlive-ntgclass
BuildRequires:	texlive-epsf
BuildRequires:	texlive-ec
BuildRequires:	texlive-cm-super
BuildRequires:	texlive-texconfig
BuildRequires:	texlive-dehyph-exptl
BuildRequires:	ghostscript
BuildRequires:	texlive
%endif

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

# build with our compile flags
sed -i -e 's|"#define COPT.*"|"#define COPT \"%{optflags} -std=c++2a\""|' ./yodl/build
sed -e "s!g++!%{__cxx}!" -e "s:#define CLS://\0:" -i yodl/verbinsert/icmconf
sed -e "s!gcc!%{__cc}!" -e "s!g++!%{__cxx}!" -i yodl/INSTALL.im

%build
export CFLAGS="%{optflags}"
export CXXFLAGS="%{optflags} -std=c++2a"
cd %{name}
./build programs
./build macros
./build man
%if %{with docs}
./build manual
%endif

%install
cd %{name}
./build install programs %{buildroot}
./build install macros %{buildroot}
./build install man %{buildroot}
%if %{with docs}
./build install manual %{buildroot}
mv -f %{buildroot}%{_docdir}/yodl-doc %{buildroot}%{_docdir}/%{name}
%endif

%files
%{_bindir}/yodl*
%{_mandir}/man*/yodl*
%{_datadir}/%{name}/*.yo
%{_datadir}/%{name}/chartables/*.tables.yo
%{_datadir}/%{name}/xml/*.xml
%{_datadir}/%{name}/xlatin1.tex
