%include	/usr/lib/rpm/macros.php
%define		_class		FSM
%define		_status		stable

%define		_pearname	%{_class}
Summary:	%{_pearname} - Finite State Machine
Summary(pl):	%{_pearname} - automat sko�czony
Name:		php-pear-%{_pearname}
Version:	1.2.4
Release:	1
Epoch:		0
License:	PHP 2.02
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	43e01067cfd468608b346553a8db923f
URL:		http://pear.php.net/package/FSM/
BuildRequires:	php-pear-PEAR
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.300
Requires:	php-pear
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The FSM package provides a simple class that implements a Finite State
Machine.

In PEAR status of this package is: %{_status}.

%description -l pl
Pakiet FSM dostarcza prost� klas� implementuj�c� automat sko�czony
(automat o sko�czonej liczbie stan�w).

Ta klasa ma w PEAR status: %{_status}.

%package tests
Summary:	Tests for PEAR::%{_pearname}
Summary(pl):	Testy dla PEAR::%{_pearname}
Group:		Development/Languages/PHP
Requires:	%{name} = %{epoch}:%{version}-%{release}
AutoReq:	no
AutoProv:	no

%description tests
Tests for PEAR::%{_pearname}.

%description tests -l pl
Testy dla PEAR::%{_pearname}.

%prep
%pear_package_setup

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}
%pear_package_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc install.log
%{php_pear_dir}/.registry/*.reg
%{php_pear_dir}/*.php

%files tests
%defattr(644,root,root,755)
%{php_pear_dir}/tests/*
