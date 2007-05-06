%define module Text-PDF
%define name  perl-%{module}
%define vers 0.29
%define subv a
%define release %mkrel 1

Summary:	 %{module} Perl module
Version:	 %{vers}%{subv}
Name:        %{name}
Release:     %{release}
Distribution:    Mandrake Linux 
License:	 Artistic
Group:		 Development/Perl
Source0:     ftp://ftp.perl.org/pub/CPAN/modules/by-module/Text//%{module}-%{version}.tar.bz2
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

