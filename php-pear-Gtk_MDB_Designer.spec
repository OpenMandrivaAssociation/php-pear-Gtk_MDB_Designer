%define		_class		Gtk
%define		_subclass	MDB
%define		upstream_name	%{_class}_%{_subclass}_Designer
%define __noautoreq /usr/bin/php

Name:		php-pear-%{upstream_name}
Version:	0.1
Release:	16
Summary:	An GTK+ Database schema designer


License:	PHP License
Group:		Development/PHP
URL:		http://pear.php.net/package/Gtk_MDB_Designer/
Source0:	http://download.pear.php.net/package/%{upstream_name}-%{version}.tar.bz2
Patch0:		php-pear-Gtk_MDB_Designer-php-gtk2.patch
Requires:	php-gtk2
Requires(post): php-pear
Requires(preun): php-pear
Requires:	php-pear
BuildArch:	noarch
BuildRequires:	php-pear

%description
A graphical database schema designer, based loosely around the MDB
schema, it features:
- table boxes which are dragged around a window to layout your
  database
- add/delete tables
- add/delete columns
- support for NotNull, Indexes, Sequences, Unique Indexes and
  defaults
- works totally in non-connected mode (eg. no database or setting up
  required)
- stores in MDB like xml file
- saves to any supported database SQL create tables files
- screenshots at http://devel.akbkhome.com/Gtk_MDB/.

%prep
%setup -q -c
%patch0 -p1
mv package.xml %{upstream_name}-%{version}/%{upstream_name}.xml

%install

cd %{upstream_name}-%{version}
pear install --nodeps --packagingroot %{buildroot} %{upstream_name}.xml
rm -rf %{buildroot}%{_datadir}/pear/.??*

rm -rf %{buildroot}%{_datadir}/pear/docs
rm -rf %{buildroot}%{_datadir}/pear/tests

install -d %{buildroot}%{_datadir}/pear/packages
install -m 644 %{upstream_name}.xml %{buildroot}%{_datadir}/pear/packages

%clean



%files
%{_bindir}/gtkmdbdesigner
%{_datadir}/pear/%{_class}
%{_datadir}/pear/packages/%{upstream_name}.xml


