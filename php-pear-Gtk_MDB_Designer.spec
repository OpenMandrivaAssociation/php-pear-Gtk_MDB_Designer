%define		_class		Gtk
%define		_subclass	MDB
%define		upstream_name	%{_class}_%{_subclass}_Designer

Name:		php-pear-%{upstream_name}
Version:	0.1
Release:	%mkrel 15
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
BuildRoot:	%{_tmppath}/%{name}-%{version}

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
rm -rf %{buildroot}

cd %{upstream_name}-%{version}
pear install --nodeps --packagingroot %{buildroot} %{upstream_name}.xml
rm -rf %{buildroot}%{_datadir}/pear/.??*

rm -rf %{buildroot}%{_datadir}/pear/docs
rm -rf %{buildroot}%{_datadir}/pear/tests

install -d %{buildroot}%{_datadir}/pear/packages
install -m 644 %{upstream_name}.xml %{buildroot}%{_datadir}/pear/packages

%clean
rm -rf %{buildroot}

%post
%if %mdkversion < 201000
pear install --nodeps --soft --force --register-only \
    %{_datadir}/pear/packages/%{upstream_name}.xml >/dev/null || :
%endif

%preun
%if %mdkversion < 201000
if [ "$1" -eq "0" ]; then
    pear uninstall --nodeps --ignore-errors --register-only \
        %{upstream_name} >/dev/null || :
fi
%endif

%files
%defattr(-,root,root)
%{_bindir}/gtkmdbdesigner
%{_datadir}/pear/%{_class}
%{_datadir}/pear/packages/%{upstream_name}.xml


%changelog
* Fri Dec 16 2011 Oden Eriksson <oeriksson@mandriva.com> 0.1-15mdv2012.0
+ Revision: 741985
- fix major breakage by careless packager

* Fri May 27 2011 Oden Eriksson <oeriksson@mandriva.com> 0.1-14
+ Revision: 679336
- mass rebuild

* Tue Dec 07 2010 Oden Eriksson <oeriksson@mandriva.com> 0.1-13mdv2011.0
+ Revision: 613664
- the mass rebuild of 2010.1 packages

* Mon Dec 14 2009 Guillaume Rousse <guillomovitch@mandriva.org> 0.1-12mdv2010.1
+ Revision: 478682
- spec cleanup
- use pear installer
- don't ship tests, even in documentation
- own all directories
- use rpm filetriggers starting from mandriva 2010.1

* Mon Sep 14 2009 Thierry Vignaud <tv@mandriva.org> 0.1-11mdv2010.0
+ Revision: 441107
- rebuild

* Thu Jan 01 2009 Oden Eriksson <oeriksson@mandriva.com> 0.1-10mdv2009.1
+ Revision: 322047
- rebuild

* Thu Jul 17 2008 Oden Eriksson <oeriksson@mandriva.com> 0.1-9mdv2009.0
+ Revision: 236846
- rebuild

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request
    - description is not a TODO list

* Wed Oct 03 2007 Oden Eriksson <oeriksson@mandriva.com> 0.1-8mdv2008.0
+ Revision: 94911
- attempt to make it use php-gtk2


* Sat Nov 11 2006 Oden Eriksson <oeriksson@mandriva.com> 0.1-7mdv2007.0
+ Revision: 81598
- Import php-pear-Gtk_MDB_Designer

* Fri Feb 10 2006 Oden Eriksson <oeriksson@mandriva.com> 0.1-7mdk
- new group (Development/PHP)

* Fri Aug 26 2005 Oden Eriksson <oeriksson@mandriva.com> 0.1-6mdk
- rebuilt to fix auto deps

* Wed Aug 10 2005 Oden Eriksson <oeriksson@mandriva.com> 0.1-5mdk
- rebuilt to use new pear auto deps/reqs from pld

* Sun Jul 31 2005 Oden Eriksson <oeriksson@mandriva.com> 0.1-4mdk
- fix deps

* Thu Jul 21 2005 Oden Eriksson <oeriksson@mandriva.com> 0.1-3mdk
- reworked the %%post and %%preun stuff, like in conectiva
- fix deps

* Wed Jul 20 2005 Oden Eriksson <oeriksson@mandriva.com> 0.1-2mdk
- fix deps

* Tue Jul 19 2005 Oden Eriksson <oeriksson@mandriva.com> 0.1-1mdk
- initial Mandriva package (PLD import)

