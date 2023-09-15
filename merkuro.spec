%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 80 ] && echo -n un; echo -n stable)

Name: merkuro
Version: 23.08.1
Release: 1
%if 0%{?git:1}
Source0:        https://invent.kde.org/pim/%{name}/-/archive/master/%{name}-master.tar.bz2
%else
Source0:        https://download.kde.org/%{stable}/release-service/%{version}/src/%{name}-%{version}.tar.xz
%endif
Summary: Calendar application to sync with external services (Nextcloud, GMail, ...)
URL: https://invent.kde.org/pim/merkuro
License: GPL
Group: User Interface/Desktops
BuildRequires: cmake ninja
BuildRequires: cmake(ECM)
BuildRequires: cmake(Qt5)
BuildRequires: cmake(Qt5Core)
BuildRequires: cmake(Qt5DBus)
BuildRequires: cmake(Qt5Gui)
BuildRequires: cmake(Qt5Svg)
BuildRequires: cmake(Qt5Qml)
BuildRequires: cmake(Qt5QmlModels)
BuildRequires: cmake(Qt5Quick)
BuildRequires: cmake(Qt5QuickControls2)
BuildRequires: cmake(Qt5QuickTest)
BuildRequires: cmake(Qt5Widgets)
BuildRequires: cmake(Qt5Network)
BuildRequires: cmake(Qt5Test)
BuildRequires: cmake(KF5CalendarCore)
BuildRequires: cmake(KF5ConfigWidgets)
BuildRequires: cmake(KF5Contacts)
BuildRequires: cmake(KF5CoreAddons)
BuildRequires: cmake(KF5DBusAddons)
BuildRequires: cmake(KF5I18n)
BuildRequires: cmake(KF5IconThemes)
BuildRequires: cmake(KF5ItemModels)
BuildRequires: cmake(KF5Kirigami2)
BuildRequires: cmake(KF5Plasma)
BuildRequires: cmake(KF5KIO)
BuildRequires: cmake(KF5QQC2DesktopStyle)
BuildRequires: cmake(KF5WindowSystem)
BuildRequires: cmake(KF5XmlGui)
BuildRequires: cmake(KF5KirigamiAddons)
BuildRequires: cmake(Freetype)
BuildRequires: cmake(Fontconfig)
BuildRequires: cmake(KPim5Akonadi)
BuildRequires: cmake(KPim5AkonadiContact)
BuildRequires: cmake(KPim5AkonadiCalendar)
BuildRequires: cmake(KPim5AkonadiMime)
BuildRequires: cmake(KPim5MailCommon)
BuildRequires: cmake(KPim5CalendarUtils)
BuildRequires: cmake(KPim5IdentityManagement)
BuildRequires: cmake(Gpgmepp)

%description
A calendar application using Akonadi to sync with external services
(Nextcloud, GMail, ...)

%prep
%autosetup -p1
%cmake_kde5 -G Ninja

%build
%ninja_build -C build

%install
%ninja_install -C build
%find_lang %{name} --all-name

%files -f %{name}.lang
%{_bindir}/merkuro-calendar
%{_bindir}/merkuro-contact
%{_bindir}/merkuro-mail
%{_datadir}/applications/org.kde.merkuro.calendar.desktop
%{_datadir}/applications/org.kde.merkuro.contact.desktop
%{_datadir}/applications/org.kde.merkuro.mail.desktop
%{_datadir}/icons/hicolor/*/*/*
%{_datadir}/metainfo/*
%{_datadir}/plasma/plasmoids/org.kde.merkuro.contact
%{_datadir}/qlogging-categories5/akonadi.quick.categories
%{_datadir}/qlogging-categories5/merkuro.categories
%{_datadir}/qlogging-categories5/merkuro.contact.categories
%{_libdir}/qt5/qml/org/kde/akonadi/*
%{_libdir}/qt5/qml/org/kde/merkuro
