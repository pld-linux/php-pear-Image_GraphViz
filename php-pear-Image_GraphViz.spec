%include	/usr/lib/rpm/macros.php
%define		_class		Image
%define		_subclass	GraphViz
%define		_pearname	%{_class}_%{_subclass}
Summary:	%{_class}_%{_subclass} - Interface to AT&T's GraphViz tools
Summary(pl):	%{_class}_%{_subclass} - interfejs do narz�dzi GraphViz AT&T
Name:		php-pear-%{_pearname}
Version:	0.2
Release:	1
License:	PHP 2.02
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
URL:		http://pear.php.net/
BuildRequires:	rpm-php-pearprov
Requires:	php-pear
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The GraphViz class allows for the creation of and the work with
directed and undirected graphs and their visualization with AT&T's
GraphViz tools.

%description -l pl
Klasa GraphViz pozwala na tworzenie oraz prac� z bezpo�rednimi i
niebezpo�rednimi grafami, a tak�e ich wizualizacj� za pomoc� narz�dzi
GraphViz AT&T.

%prep
%setup -q -c

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}

install %{_pearname}-%{version}/*.php $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{php_pear_dir}/%{_class}/*.php
