%include        /usr/lib/rpm/macros.php
%define		_class		FSM
%define		_status		stable

%define		_pearname	%{_class}
Summary:	%{_pearname} - Finite State Machine
Summary(pl):	%{_pearname} - automat skoñczony
Name:		php-pear-%{_pearname}
Version:	1.2.1
Release:	1
License:	PHP 2.02
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	ed59d34836efe0dd3fb26266c3bb54e8
URL:		http://pear.php.net/package/FSM/
BuildRequires:	rpm-php-pearprov >= 4.0.2-98
Requires:	php-pear
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The FSM package provides a simple class that implements a Finite State
Machine.

This class has in PEAR status: %{_status}.

%description -l pl
Pakiet FSM dostarcza prost± klasê implementuj±c± automat skoñczony
(automat o skoñczonej liczbie stanów).

Ta klasa ma w PEAR status: %{_status}.

%prep
%setup -q -c

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}/%{_pearname}

install %{_pearname}-%{version}/*.php $RPM_BUILD_ROOT%{php_pear_dir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{php_pear_dir}/*.php
