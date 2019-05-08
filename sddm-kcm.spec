#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0xEC94D18F7F05997E (jr@jriddell.org)
#
Name     : sddm-kcm
Version  : 5.15.5
Release  : 7
URL      : https://download.kde.org/stable/plasma/5.15.5/sddm-kcm-5.15.5.tar.xz
Source0  : https://download.kde.org/stable/plasma/5.15.5/sddm-kcm-5.15.5.tar.xz
Source99 : https://download.kde.org/stable/plasma/5.15.5/sddm-kcm-5.15.5.tar.xz.sig
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
BuildRequires : libX11-dev libICE-dev libSM-dev libXau-dev libXcomposite-dev libXcursor-dev libXdamage-dev libXdmcp-dev libXext-dev libXfixes-dev libXft-dev libXi-dev libXinerama-dev libXi-dev libXmu-dev libXpm-dev libXrandr-dev libXrender-dev libXres-dev libXScrnSaver-dev libXt-dev libXtst-dev libXv-dev libXxf86misc-dev libXxf86vm-dev
BuildRequires : qtbase-dev mesa-dev

%description
mkdir build
cd build
cmake .. -DCMAKE_INSTALL_PREFIX=`kde4-config --prefix`
make install

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
%setup -q -n sddm-kcm-5.15.5

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1557344657
mkdir -p clr-build
pushd clr-build
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
%cmake ..
make  %{?_smp_mflags}
popd

%install
export SOURCE_DATE_EPOCH=1557344657
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/sddm-kcm
cp COPYING %{buildroot}/usr/share/package-licenses/sddm-kcm/COPYING
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
/usr/share/kservices5/kcm_sddm.desktop
/usr/share/polkit-1/actions/org.kde.kcontrol.kcmsddm.policy
/usr/share/sddm-kcm/main.qml
/usr/share/xdg/sddmtheme.knsrc

%files lib
%defattr(-,root,root,-)
/usr/lib64/qt5/plugins/kcm_sddm.so

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/sddm-kcm/COPYING

%files locales -f kcm_sddm.lang
%defattr(-,root,root,-)

