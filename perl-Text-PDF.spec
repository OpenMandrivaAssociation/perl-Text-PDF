%define module Text-PDF
%define name  perl-%{module}
%define vers 0.29
%define subv a
%define release %mkrel 6

Summary:	 %{module} Perl module
Version:	 %perl_convert_version 0.29a
Name:        %{name}
Release:     1
License:	 Artistic
Group:		 Development/Perl
Source0:     ftp://ftp.perl.org:21/pub/CPAN/modules/by-module/Text/Text-PDF-0.29a.tar.gz
URL:		 http://search.cpan.org/dist/%{module}
BuildRoot:	 %{_tmppath}/%name-%version-buildroot
BuildRequires: perl-devel
BuildArch: noarch

%description
Perl module to manipulate PDF files.

%prep
%setup -q -n %{module}-%{vers}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor

%check
# no test defined yet
%make test

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc examples readme.txt 
%{_mandir}/*/*
%{perl_vendorlib}/Text/
%{_bindir}/*



%changelog
* Tue May 03 2011 Michael Scherer <misc@mandriva.org> 0.29a-6mdv2011.0
+ Revision: 664901
- mass rebuild

* Fri Sep 04 2009 Thierry Vignaud <tv@mandriva.org> 0.29a-5mdv2010.0
+ Revision: 430603
- rebuild

* Thu Jul 31 2008 Thierry Vignaud <tv@mandriva.org> 0.29a-4mdv2009.0
+ Revision: 258619
- rebuild

* Thu Jul 24 2008 Thierry Vignaud <tv@mandriva.org> 0.29a-3mdv2009.0
+ Revision: 246637
- rebuild

* Wed Jan 02 2008 Olivier Blin <oblin@mandriva.com> 0.29a-1mdv2008.1
+ Revision: 140721
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Mon May 07 2007 Olivier Thauvin <nanardon@mandriva.org> 0.29a-1mdv2008.0
+ Revision: 23801
- kill Distribution tag from spec
- 0.29a


* Fri Apr 28 2006 Nicolas Lécureuil <neoclust@mandriva.org> 0.25-2mdk
- Fix SPEC according to Perl Policy
	- Source URL
- use mkrel

* Thu Dec 25 2003 Michael Scherer <misc@mandrake.org> 0.25-1mdk 
- introdution in contribs, based on Daniel Lacroix <dlacroix@erasme.org> work


