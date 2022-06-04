#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-POE-Test-Loops
Version  : 1.360
Release  : 13
URL      : https://cpan.metacpan.org/authors/id/R/RC/RCAPUTO/POE-Test-Loops-1.360.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/R/RC/RCAPUTO/POE-Test-Loops-1.360.tar.gz
Summary  : 'Reusable tests for POE::Loop authors'
Group    : Development/Tools
License  : Artistic-1.0 Artistic-1.0-Perl GPL-1.0
Requires: perl-POE-Test-Loops-bin = %{version}-%{release}
Requires: perl-POE-Test-Loops-license = %{version}-%{release}
Requires: perl-POE-Test-Loops-man = %{version}-%{release}
Requires: perl-POE-Test-Loops-perl = %{version}-%{release}
BuildRequires : buildreq-cpan

%description
NAME
POE::Test::Loops - Reusable tests for POE::Loop authors
SYNOPSIS
#!/usr/bin/perl -w

%package bin
Summary: bin components for the perl-POE-Test-Loops package.
Group: Binaries
Requires: perl-POE-Test-Loops-license = %{version}-%{release}

%description bin
bin components for the perl-POE-Test-Loops package.


%package dev
Summary: dev components for the perl-POE-Test-Loops package.
Group: Development
Requires: perl-POE-Test-Loops-bin = %{version}-%{release}
Provides: perl-POE-Test-Loops-devel = %{version}-%{release}
Requires: perl-POE-Test-Loops = %{version}-%{release}

%description dev
dev components for the perl-POE-Test-Loops package.


%package license
Summary: license components for the perl-POE-Test-Loops package.
Group: Default

%description license
license components for the perl-POE-Test-Loops package.


%package man
Summary: man components for the perl-POE-Test-Loops package.
Group: Default

%description man
man components for the perl-POE-Test-Loops package.


%package perl
Summary: perl components for the perl-POE-Test-Loops package.
Group: Default
Requires: perl-POE-Test-Loops = %{version}-%{release}

%description perl
perl components for the perl-POE-Test-Loops package.


%prep
%setup -q -n POE-Test-Loops-1.360
cd %{_builddir}/POE-Test-Loops-1.360

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/perl-POE-Test-Loops
cp %{_builddir}/POE-Test-Loops-1.360/LICENSE %{buildroot}/usr/share/package-licenses/perl-POE-Test-Loops/8de7eb82c879aaea94684487146e60ebdddca0db
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/poe-gen-tests

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/POE::Test::Loops.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/perl-POE-Test-Loops/8de7eb82c879aaea94684487146e60ebdddca0db

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/poe-gen-tests.1

%files perl
%defattr(-,root,root,-)
/usr/lib/perl5/*
