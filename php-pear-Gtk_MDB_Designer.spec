%define		_class		Gtk
%define		_subclass	MDB
%define		_status		beta
%define		_pearname	%{_class}_%{_subclass}_Designer

Summary:	%{_pearname} - an GTK+ Database schema designer
Name:		php-pear-%{_pearname}
Version:	0.1
Release:	%mkrel 11
License:	PHP License
Group:		Development/PHP
URL:		http://pear.php.net/package/Gtk_MDB_Designer/
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tar.bz2
Patch0:		php-pear-Gtk_MDB_Designer-php-gtk2.diff
Requires:	php-gtk2
Requires(post): php-pear
Requires(preun): php-pear
Requires:	php-pear
BuildArch:	noarch
BuildRequires:	dos2unix
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

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

In PEAR status of this package is: %{_status}.

%prep

%setup -q -c

find . -type d -perm 0700 -exec chmod 755 {} \;
find . -type f -perm 0555 -exec chmod 755 {} \;
find . -type f -perm 0444 -exec chmod 644 {} \;

for i in `find . -type d -name CVS` `find . -type f -name .cvs\*` `find . -type f -name .#\*`; do
    if [ -e "$i" ]; then rm -rf $i; fi >&/dev/null
done

# strip away annoying ^M
find -type f | grep -v ".gif" | grep -v ".png" | grep -v ".jpg" | xargs dos2unix -U

%patch0 -p0

%install
rm -rf %{buildroot}

install -d %{buildroot}%{_datadir}/pear/%{_class}/%{_subclass}/Designer/Interface

install %{_pearname}-%{version}/*.php %{buildroot}%{_datadir}/pear/%{_class}/%{_subclass}
install %{_pearname}-%{version}/Designer/*.{php,glade} %{buildroot}%{_datadir}/pear/%{_class}/%{_subclass}/Designer
install %{_pearname}-%{version}/Designer/Interface/* %{buildroot}%{_datadir}/pear/%{_class}/%{_subclass}/Designer/Interface

install -d %{buildroot}%{_datadir}/pear/packages
install -m0644 package.xml %{buildroot}%{_datadir}/pear/packages/%{_pearname}.xml

%post
if [ "$1" = "1" ]; then
	if [ -x %{_bindir}/pear -a -f %{_datadir}/pear/packages/%{_pearname}.xml ]; then
		%{_bindir}/pear install --nodeps -r %{_datadir}/pear/packages/%{_pearname}.xml
	fi
fi
if [ "$1" = "2" ]; then
	if [ -x %{_bindir}/pear -a -f %{_datadir}/pear/packages/%{_pearname}.xml ]; then
		%{_bindir}/pear upgrade -f --nodeps -r %{_datadir}/pear/packages/%{_pearname}.xml
	fi
fi

%preun
if [ "$1" = 0 ]; then
	if [ -x %{_bindir}/pear -a -f %{_datadir}/pear/packages/%{_pearname}.xml ]; then
		%{_bindir}/pear uninstall --nodeps -r %{_pearname}
	fi
fi

%clean
rm -rf %{buildroot}

%files
%defattr(644,root,root,755)
%{_datadir}/pear/%{_class}/%{_subclass}/Designer.php
%{_datadir}/pear/%{_class}/%{_subclass}/Designer
%{_datadir}/pear/packages/%{_pearname}.xml
