%define		_status		stable
%define		_pearname	Image_GraphViz
Summary:	%{_pearname} - Interface to AT&T's GraphViz tools
Summary(pl.UTF-8):	%{_pearname} - interfejs do narzędzi GraphViz AT&T
Name:		php-pear-%{_pearname}
Version:	1.3.0
Release:	1
License:	PHP 2.02
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	b6ed7a04682818c36aab775f8392005f
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

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc install.log
%{php_pear_dir}/.registry/*.reg
%{php_pear_dir}/Image/*.php
