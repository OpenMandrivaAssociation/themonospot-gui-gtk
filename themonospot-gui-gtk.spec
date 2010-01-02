Summary   : Gtk application to use themonospot (multimedia files parser/editor)
Name      : themonospot-gui-gtk
Version   : 0.2.2
Release   : %mkrel 1
License   : GPLv2
Group     : Video
Source    : http://www.integrazioneweb.com/repository/SOURCES/themonospot-gui-gtk-%{version}.tar.gz
BuildRoot : %{_tmppath}/%{name}-%{version}-%{release}-buildroot
URL       : http://www.integrazioneweb.com/themonospot

#BuildArch : noarch

BuildRequires: mono-devel
BuildRequires: themonospot-base-devel
BuildRequires: gtk-sharp2
BuildRequires: glade-sharp2



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
* Wed Dec 30 2009 Armando Basile <hmandevteam@gmail.com> 0.2.2-1mdv2010.1
- removed GAC use
- bug fix: scan process without plugin installed

* Mon Dec 14 2009 Armando Basile <hmandevteam@gmail.com> 0.2.0-1mdv2010.1
- first release of new Gtk application to use themonospot