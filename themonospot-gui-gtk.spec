# mono...
%define debug_package %{nil}

Summary: Gtk application to use themonospot (multimedia files parser/editor)
Name:    themonospot-gui-gtk
Version: 0.2.2
Release: 7
License: GPLv2
Group:   Video
Source:  http://www.integrazioneweb.com/repository/SOURCES/themonospot-gui-gtk-%{version}.tar.gz
Patch0:  themonospot-gui-gtk-0.2.2-drop-invalid-dekstop-item-patch
Url:     https://www.integrazioneweb.com/themonospot
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
%makeinstall_std

%files
%doc copying.gpl
%{_bindir}/themonospot-gtk
%{_libdir}/themonospot/%{name}.exe
%{_datadir}/pixmaps/themonospot-gtk.png
%{_datadir}/applications/themonospot-gtk.desktop
