#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : sddm-kcm
Version  : 5.23.0
Release  : 41
URL      : https://download.kde.org/stable/plasma/5.23.0/sddm-kcm-5.23.0.tar.xz
Source0  : https://download.kde.org/stable/plasma/5.23.0/sddm-kcm-5.23.0.tar.xz
Summary  : No detailed summary available
Group    : Development/Tools
License  : CC0-1.0 GPL-2.0 GPL-3.0
Requires: sddm-kcm-bin = %{version}-%{release}
Requires: sddm-kcm-data = %{version}-%{release}
Requires: sddm-kcm-lib = %{version}-%{release}
Requires: sddm-kcm-license = %{version}-%{release}
Requires: sddm-kcm-locales = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : buildreq-kde
BuildRequires : extra-cmake-modules-data
BuildRequires : ki18n-dev
BuildRequires : qtbase-dev mesa-dev

%description
# sddm-kcm - Login Screen (SDDM) System Settings Module
`sddm-kcm` is a KConfig Module (KCM) that integrates itself into KDE's System Settings and serves the purpose of configuring the Simple Desktop Display Manager (SDDM) - the recommended display manager for KDE Plasma.

%package bin
Summary: bin components for the sddm-kcm package.
Group: Binaries
Requires: sddm-kcm-data = %{version}-%{release}
Requires: sddm-kcm-license = %{version}-%{release}

%description bin
bin components for the sddm-kcm package.


%package data
Summary: data components for the sddm-kcm package.
Group: Data

%description data
data components for the sddm-kcm package.


%package lib
Summary: lib components for the sddm-kcm package.
Group: Libraries
Requires: sddm-kcm-data = %{version}-%{release}
Requires: sddm-kcm-license = %{version}-%{release}

%description lib
lib components for the sddm-kcm package.


%package license
Summary: license components for the sddm-kcm package.
Group: Default

%description license
license components for the sddm-kcm package.


%package locales
Summary: locales components for the sddm-kcm package.
Group: Default

%description locales
locales components for the sddm-kcm package.


%prep
%setup -q -n sddm-kcm-5.23.0
cd %{_builddir}/sddm-kcm-5.23.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1634393418
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
%cmake ..
make  %{?_smp_mflags}
popd

%install
export SOURCE_DATE_EPOCH=1634393418
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/sddm-kcm
cp %{_builddir}/sddm-kcm-5.23.0/COPYING %{buildroot}/usr/share/package-licenses/sddm-kcm/4cc77b90af91e615a64ae04893fdffa7939db84c
cp %{_builddir}/sddm-kcm-5.23.0/LICENSES/CC0-1.0.txt %{buildroot}/usr/share/package-licenses/sddm-kcm/82da472f6d00dc5f0a651f33ebb320aa9c7b08d0
cp %{_builddir}/sddm-kcm-5.23.0/LICENSES/GPL-2.0-or-later.txt %{buildroot}/usr/share/package-licenses/sddm-kcm/3e8971c6c5f16674958913a94a36b1ea7a00ac46
cp %{_builddir}/sddm-kcm-5.23.0/LICENSES/GPL-3.0-only.txt %{buildroot}/usr/share/package-licenses/sddm-kcm/e3bdbf20d43fc066a1b40a64d57d4ae5a31f177f
cp %{_builddir}/sddm-kcm-5.23.0/LICENSES/LicenseRef-KDE-Accepted-GPL.txt %{buildroot}/usr/share/package-licenses/sddm-kcm/7d9831e05094ce723947d729c2a46a09d6e90275
cp %{_builddir}/sddm-kcm-5.23.0/LICENSES/LicenseRef-KDE-Accepted-GPL.txt %{buildroot}/usr/share/package-licenses/sddm-kcm/7d9831e05094ce723947d729c2a46a09d6e90275
pushd clr-build
%make_install
popd
%find_lang kcm_sddm

%files
%defattr(-,root,root,-)
/usr/lib64/libexec/kauth/kcmsddm_authhelper

%files bin
%defattr(-,root,root,-)
/usr/bin/sddmthemeinstaller

%files data
%defattr(-,root,root,-)
/usr/share/dbus-1/system-services/org.kde.kcontrol.kcmsddm.service
/usr/share/dbus-1/system.d/org.kde.kcontrol.kcmsddm.conf
/usr/share/knsrcfiles/sddmtheme.knsrc
/usr/share/kpackage/kcms/kcm_sddm/contents/ui/Advanced.qml
/usr/share/kpackage/kcms/kcm_sddm/contents/ui/DetailsDialog.qml
/usr/share/kpackage/kcms/kcm_sddm/contents/ui/main.qml
/usr/share/kpackage/kcms/kcm_sddm/metadata.desktop
/usr/share/kpackage/kcms/kcm_sddm/metadata.json
/usr/share/kservices5/kcm_sddm.desktop
/usr/share/polkit-1/actions/org.kde.kcontrol.kcmsddm.policy

%files lib
%defattr(-,root,root,-)
/usr/lib64/qt5/plugins/kcms/kcm_sddm.so

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/sddm-kcm/3e8971c6c5f16674958913a94a36b1ea7a00ac46
/usr/share/package-licenses/sddm-kcm/4cc77b90af91e615a64ae04893fdffa7939db84c
/usr/share/package-licenses/sddm-kcm/7d9831e05094ce723947d729c2a46a09d6e90275
/usr/share/package-licenses/sddm-kcm/82da472f6d00dc5f0a651f33ebb320aa9c7b08d0
/usr/share/package-licenses/sddm-kcm/e3bdbf20d43fc066a1b40a64d57d4ae5a31f177f

%files locales -f kcm_sddm.lang
%defattr(-,root,root,-)

