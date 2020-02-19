#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0xEC94D18F7F05997E (jr@jriddell.org)
#
Name     : sddm-kcm
Version  : 5.18.1
Release  : 22
URL      : https://download.kde.org/stable/plasma/5.18.1/sddm-kcm-5.18.1.tar.xz
Source0  : https://download.kde.org/stable/plasma/5.18.1/sddm-kcm-5.18.1.tar.xz
Source1  : https://download.kde.org/stable/plasma/5.18.1/sddm-kcm-5.18.1.tar.xz.sig
Summary  : KDE Config Module for SDDM
Group    : Development/Tools
License  : GPL-2.0
Requires: sddm-kcm-bin = %{version}-%{release}
Requires: sddm-kcm-data = %{version}-%{release}
Requires: sddm-kcm-lib = %{version}-%{release}
Requires: sddm-kcm-license = %{version}-%{release}
Requires: sddm-kcm-locales = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : buildreq-kde
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
%setup -q -n sddm-kcm-5.18.1
cd %{_builddir}/sddm-kcm-5.18.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1582087621
mkdir -p clr-build
pushd clr-build
# -Werror is for werrorists
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
%cmake ..
make  %{?_smp_mflags}  VERBOSE=1
popd

%install
export SOURCE_DATE_EPOCH=1582087621
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/sddm-kcm
cp %{_builddir}/sddm-kcm-5.18.1/COPYING %{buildroot}/usr/share/package-licenses/sddm-kcm/4cc77b90af91e615a64ae04893fdffa7939db84c
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
/usr/share/kservices5/kcm_sddm.desktop
/usr/share/polkit-1/actions/org.kde.kcontrol.kcmsddm.policy
/usr/share/sddm-kcm/main.qml

%files lib
%defattr(-,root,root,-)
/usr/lib64/qt5/plugins/kcm_sddm.so

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/sddm-kcm/4cc77b90af91e615a64ae04893fdffa7939db84c

%files locales -f kcm_sddm.lang
%defattr(-,root,root,-)

