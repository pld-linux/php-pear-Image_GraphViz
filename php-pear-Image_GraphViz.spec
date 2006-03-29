%include	/usr/lib/rpm/macros.php
%define		_class		Image
%define		_subclass	GraphViz
%define		_status		stable
%define		_pearname	%{_class}_%{_subclass}

Summary:	%{_pearname} - Interface to AT&T's GraphViz tools
Summary(pl):	%{_pearname} - interfejs do narzêdzi GraphViz AT&T
Name:		php-pear-%{_pearname}
Version:	1.1.0
Release:	3
License:	PHP 2.02
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	05602e2c2341dce9abc36e96ce367c84
URL:		http://pear.php.net/package/Image_GraphViz/
BuildRequires:	php-pear-PEAR
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
Requires:	php-pear
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The GraphViz class allows for the creation of and the work with
directed and undirected graphs and their visualization with AT&T's
GraphViz tools.

In PEAR status of this package is: %{_status}.

%description -l pl
Klasa GraphViz pozwala na tworzenie oraz pracê z bezpo¶rednimi i
niebezpo¶rednimi grafami, a tak¿e ich wizualizacjê za pomoc± narzêdzi
GraphViz AT&T.

Ta klasa ma w PEAR status: %{_status}.

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
%{php_pear_dir}/%{_class}/*.php
