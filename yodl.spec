%define	name	yodl
%define version 3.00.0

Summary:	Your Own Document Language
Name:		%{name}
Version:	%{version}
Release:	8
License:	GPLv3
Group:		Text tools
URL:		http://yodl.sourceforge.net
Source0:		http://downloads.sourceforge.net/project/yodl/%{name}/%{version}/%{name}_%{version}.orig.tar.gz
Prefix:		%{_prefix}
BuildRequires:	bison, flex, diffutils, groff-for-man, libtool, netpbm, python, texinfo, icmake
BuildRequires:	texlive-latex texlive-ntgclass texlive-epsf texlive-ec texlive-cm-super
BuildRequires:	ghostscript

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
%defattr(-,root,root)
%doc README.txt README.3.00.0
%{_bindir}/yodl*
%{_mandir}/man*/yodl*
%{_datadir}/%{name}/*.yo
%{_datadir}/%{name}/chartables/*.tables.yo
%{_datadir}/%{name}/xml/*.xml
%{_datadir}/%{name}/xlatin1.tex


%changelog
* Wed Dec 21 2011 Dmitry Mikhirev <dmikhirev@mandriva.org> 3.00.0-1mdv2012.0
+ Revision: 744203
- BR ghostscript for the same reason
- BR ghostscript-common to fix docs build
- use %%setup_compile_flags
- new tarball
- update to 3.00.0

* Sat May 07 2011 Oden Eriksson <oeriksson@mandriva.com> 1.31.18-17
+ Revision: 671945
- mass rebuild

* Sat Dec 04 2010 Oden Eriksson <oeriksson@mandriva.com> 1.31.18-16mdv2011.0
+ Revision: 608252
- rebuild

* Wed Mar 17 2010 Oden Eriksson <oeriksson@mandriva.com> 1.31.18-15mdv2010.1
+ Revision: 524478
- rebuilt for 2010.1

  + JÃ©rÃ´me Brenier <incubusss@mandriva.org>
    - revert to r179435, new version doesn't build zsh guide
    - new version 2.15.1
    - doc subpackage added
    - numerous changes to adapt the specfile to this new version
      (new build process, new files, new buildrequires...)
    - license tag fixed

* Wed Mar 05 2008 Oden Eriksson <oeriksson@mandriva.com> 1.31.18-14mdv2008.1
+ Revision: 179435
- rebuild

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request
    - fix summary-ended-with-dot

* Mon Apr 30 2007 Andrey Borzenkov <arvidjaar@mandriva.org> 1.31.18-13mdv2008.0
+ Revision: 19486
- rebuild
- Import yodl



* Sun Jan 01 2006 Mandriva Linux Team <http://www.mandrivaexpert.com/> 1.31.18-12mdk
- Rebuild

* Thu Jun 02 2005 Nicolas Lécureuil <neoclust@mandriva.org> 1.31.18-11mdk
- Rebuild

* Tue May 04 2004 Thierry Vignaud <tvignaud@mandrakesoft.com> 1.31.18-10mdk
- relink with new libintl

* Thu Jul 24 2003 Per Øyvind Karlsen <peroyvind@sintrax.net> 1.31.18-9mdk
- rebuild

* Fri Jan 17 2003 Gwenole Beauchesne <gbeauchesne@mandrakesoft.com> 1.31.18-8mdk
- Rebuild

* Wed May 29 2002 Gwenole Beauchesne <gbeauchesne@mandrakesoft.com> 1.31.18-7mdk
- Automated rebuild with gcc 3.1-1mdk

* Thu Dec  6 2001 Gwenole Beauchesne <gbeauchesne@mandrakesoft.com> 1.31.18-6mdk
- Still make rpmlint happy: invalid-packager, zero-length files

* Sun Oct 14 2001 Stefan van der Eijk <stefan@eijk.nu> 1.31.18-5mdk
- BuildRequires: netpbm

* Thu Aug 16 2001 Gwenole Beauchesne <gbeauchesne@mandrakesoft.com> 1.31.18-4mdk
- Set datadir to %%{_datadir}/yodl
- Sanitize specfile (s/Copyright/License/)

* Wed Jun 27 2001 Matthias Badaire <mbadaire@mandrakesoft.com> 1.31.18-3mdk
- Fix yodl2html for ia64  : missing includes

* Tue Apr 10 2001 Gwenole Beauchesne <gbeauchesne@mandrakesoft.com> 1.31.18-2mdk
- sanitized specfile (BuildRequires, files section, etc.)

* Wed Jul 19 2000 Chmouel Boudjnah <chmouel@mandrakesoft.com> 1.31.18-1mdk
- 1.32.18.
- BM.

* Tue Jun 20 2000 Chmouel Boudjnah <chmouel@mandrakesoft.com> 1.31.17-4mdk
- Use makeinstall macros.

* Wed May 31 2000 Chmouel Boudjnah <chmouel@mandrakesoft.com> 1.31.17-3mdk
- Clean up specs.

* Thu May 04 2000 Lenny Cartier <lenny@mandrakesoft.com> 1.31.17-2mdk
- fix group
