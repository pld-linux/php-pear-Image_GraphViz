%include	/usr/lib/rpm/macros.php
%define		_class		Image
%define		_subclass	GraphViz
%define		_status		beta
%define		_pearname	%{_class}_%{_subclass}
%define		subver	RC3
%define		rel		1
Summary:	%{_pearname} - Interface to AT&T's GraphViz tools
Summary(pl.UTF-8):	%{_pearname} - interfejs do narzędzi GraphViz AT&T
Name:		php-pear-%{_pearname}
Version:	1.3.0
Release:	0.%{subver}.%{rel}
License:	PHP 2.02
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}%{subver}.tgz
# Source0-md5:	59f4d88f0479dee91079ffbd59eb5ed4
URL:		http://pear.php.net/package/Image_GraphViz/
BuildRequires:	php-pear-PEAR
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.300
Requires:	php-pear
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The GraphViz class allows for the creation of and the work with
directed and undirected graphs and their visualization with AT&T's
GraphViz tools.

In PEAR status of this package is: %{_status}.

%description -l pl.UTF-8
Klasa GraphViz pozwala na tworzenie oraz pracę z bezpośrednimi i
niebezpośrednimi grafami, a także ich wizualizację za pomocą narzędzi
GraphViz AT&T.

Ta klasa ma w PEAR status: %{_status}.

%prep
%pear_package_setup

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}
%pear_package_install

# don't care for tests
rm -rf $RPM_BUILD_ROOT%{php_pear_dir}/tests/%{_pearname}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc install.log
%{php_pear_dir}/.registry/*.reg
%{php_pear_dir}/%{_class}/*.php
