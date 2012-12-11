%define upstream_name    IO-Tty-Util
%define upstream_version 0.03

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:	4

Summary:    No summary found
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/IO/%{upstream_name}-%{upstream_version}.tar.gz


BuildRequires: perl-devel
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}

%description
the IO::Tty::Util manpage provides basic Perl bindings to the 'openpty' and
'login_tty' functions found in 'libutil.so' and provides a Perl
implementation of the 'forkpty' function.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
# tests seem to fail with perl 5.12 without tty (such as the bs)
#make test

%install
rm -rf %buildroot
%makeinstall_std

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc Changes README
%{_mandir}/man3/*
%perl_vendorlib/*


%changelog
* Wed Jan 25 2012 Per Øyvind Karlsen <peroyvind@mandriva.org> 0.30.0-4
+ Revision: 768358
- svn commit -m mass rebuild of perl extension against perl 5.14.2

* Sat Jul 24 2010 Jérôme Quelin <jquelin@mandriva.org> 0.30.0-3mdv2011.0
+ Revision: 558102
- skip tests, they need a tty with perl 5.12
- rebuild
- rebuild for perl 5.12

* Thu Oct 01 2009 Jérôme Quelin <jquelin@mandriva.org> 0.30.0-1mdv2010.0
+ Revision: 452087
- import perl-IO-Tty-Util


* Thu Oct 01 2009 cpan2dist 0.03-1mdv
- initial mdv release, generated with cpan2dist
