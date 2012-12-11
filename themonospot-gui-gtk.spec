Summary: Gtk application to use themonospot (multimedia files parser/editor)
Name: themonospot-gui-gtk
Version: 0.2.2
Release: %mkrel 5
License: GPLv2
Group: Video
Source: http://www.integrazioneweb.com/repository/SOURCES/themonospot-gui-gtk-%{version}.tar.gz
Patch0: themonospot-gui-gtk-0.2.2-drop-invalid-dekstop-item-patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
URL: http://www.integrazioneweb.com/themonospot
BuildRequires: mono-devel
BuildRequires: themonospot-base-devel
BuildRequires: gtk-sharp2
BuildRequires: glade-sharp2

%description
themonospot-gui-gtk is a Mono framework application to create a
graphic frontend to use themonospot base component and his plugins.

%prep
%setup -q
%patch0 -p0 -b .orig
chmod 0644 src/resources/*

%build
%configure2_5x
%make

%install
rm -fr %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc copying.gpl
%{_bindir}/themonospot-gtk
%{_libdir}/themonospot/%{name}.exe
%{_datadir}/pixmaps/themonospot-gtk.png
%{_datadir}/applications/themonospot-gtk.desktop


%changelog
* Wed Dec 08 2010 Oden Eriksson <oeriksson@mandriva.com> 0.2.2-5mdv2011.0
+ Revision: 615209
- the mass rebuild of 2010.1 packages

* Sun May 02 2010 Funda Wang <fwang@mandriva.org> 0.2.2-4mdv2010.1
+ Revision: 541542
- fix mod of resource files

* Sat May 01 2010 Funda Wang <fwang@mandriva.org> 0.2.2-3mdv2010.1
+ Revision: 541460
- more invalid item removed

* Mon Feb 22 2010 Funda Wang <fwang@mandriva.org> 0.2.2-2mdv2010.1
+ Revision: 509778
- fix desktop file

* Sat Jan 02 2010 Armando Basile <hman@mandriva.org> 0.2.2-1mdv2010.1
+ Revision: 485134
- removed GAC use
- bug fix: scan process without plugin installed

* Thu Dec 24 2009 Armando Basile <hman@mandriva.org> 0.2.0-1mdv2010.1
+ Revision: 482034
- first public release of Gtk gui application for new Themonospot suite
- create themonospot-gui-gtk

