Summary   : Gtk application to use themonospot (multimedia files parser/editor)
Name      : themonospot-gui-gtk
Version   : 0.2.0
Release   : %mkrel 1
License   : GPLv2
Group     : Video
Source    : http://www.integrazioneweb.com/repository/SOURCES/themonospot-gui-gtk-%{version}.tar.gz
BuildRoot : %{_tmppath}/%{name}-%{version}-%{release}-buildroot
URL       : http://www.integrazioneweb.com/themonospot

#BuildArch : noarch

BuildRequires: mono >= 1.2.3
BuildRequires: gtk-sharp2 >= 2.8.3
BuildRequires: glade-sharp2 >= 2.8.3
BuildRequires: themonospot-base
BuildRequires: pkgconfig

Requires: gtk-sharp2 >= 2.8.3
Requires: glade-sharp2 >= 2.8.3
Requires: glib-sharp2 >= 2.8.3
Requires: themonospot-base
Requires: mono >= 1.2.3


%description
themonospot-gui-gtk is a Mono framework application to create a
graphic frontend to use themonospot base component and his plugins.

%prep
%setup -q

%build
%configure2_5x
%make

%install
rm -fr %{buildroot}
#%makeinstall_std linuxpkgconfigdir=%{_datadir}/pkgconfig
%makeinstall_std


%clean
rm -rf %{buildroot}


%files
%defattr(-,root,root,-)
%{_bindir}/themonospot-gtk
%{_libdir}/%{name}/
%{_datadir}/pixmaps/themonospot-gtk.png
%{_datadir}/applications/themonospot-gtk.desktop


%changelog
* Mon Dec 14 2009 Armando Basile <hmandevteam@gmail.com> 0.2.0-1mdv2010.1
- first release of new Gtk application to use themonospot
