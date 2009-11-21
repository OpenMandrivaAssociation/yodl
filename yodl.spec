%define version 2.15.1

Summary:	Yet oneOther Document Language
Name:		yodl
Version:	%{version}
Release:	%mkrel 1
License:	GPLv3
Group:		Text tools
URL:		http://yodl.sourceforge.net/
Source:		http://downloads.sourceforge.net/project/%{name}/%{name}/%{version}/%{name}_%{version}.orig.tar.gz
BuildRoot:	%{_tmppath}/%{name}-%{version}
BuildRequires:	tetex-latex
BuildRequires:	icmake

%description
Yodl is a package implementing a pre-document language and tools to 
process it. The idea of Yodl is that you write up a document in a 
pre-language, then use the tools (e.g. yodl2html) to convert it to 
some final document language. Current converters are for HTML, man, 
LaTeX, a poor-man's text converter and an experimental XML converter. 
Main document types are `article', `report', `book', `letter' and 
`manpage'. The Yodl document language is designed to be easy to use 
and extensible.

%package	doc
Summary:	Yet oneOther Document Language documentation
Group:		Text tools

%description	doc
Documentation for yodl Yet oneOther Document Language.

%prep
%setup -q

%build
./build programs
./build man
./build manual
./build macros

%install
if [ -d %{buildroot} ]; then rm -rf %{buildroot}; fi
./build install programs %{buildroot}
./build install man %{buildroot}
./build install manual %{buildroot}
./build install macros %{buildroot}
./build install docs %{buildroot}               

%clean
if [ -d %{buildroot} ]; then rm -rf %{buildroot}; fi

%files
%defattr(-,root,root)
%doc AUTHORS.txt README.txt changelog CHANGES
%{_bindir}/yodl
%{_bindir}/yodlpost
%{_bindir}/yodlstriproff
%{_bindir}/yodlverbinsert
%{_bindir}/yodl2html
%{_bindir}/yodl2latex
%{_bindir}/yodl2man
%{_bindir}/yodl2txt
%{_bindir}/yodl2whatever
%{_bindir}/yodl2xml
%{_mandir}/man*/yodl*
%{_datadir}/yodl

%files		doc
%defattr(-,root,root,-)
%{_docdir}/%{name}-doc
