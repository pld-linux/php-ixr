%define		php_min_version 5.0.0
%include	/usr/lib/rpm/macros.php
Summary:	The Incutio XML-RPC Library for PHP
Name:		php-ixr
Version:	1.7.4
Release:	1
License:	BSD
Group:		Development/Languages/PHP
Source0:	http://php-ixr.googlecode.com/files/%{name}-%{version}.tar.gz
# Source0-md5:	4daf00b83611ffeeb6d86be0ac152508
URL:		http://scripts.incutio.com/xmlrpc/
BuildRequires:	/usr/bin/php
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.461
Requires:	php(core) >= %{php_min_version}
Requires:	php(date)
Requires:	php(pcre)
Requires:	php(xml)
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The Incutio XML-RPC library (IXR) is designed primarily for ease of
use. It incorporates both client and server classes, and is designed
to hide as much of the workings of XML-RPC from the user as possible.
A key feature of the library is automatic type conversion from PHP
types to XML-RPC types and vice versa. This should enable developers
to write web services with very little knowledge of the underlying
XML-RPC standard.

Don't however be fooled by it's simple surface. The library includes a
wide variety of additional XML-RPC specifications and has all of the
features required for serious web service implementations.

%prep
%setup -qc

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_data_dir}
cp -p IXR_Library.php $RPM_BUILD_ROOT%{php_data_dir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{php_data_dir}/IXR_Library.php
