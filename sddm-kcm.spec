#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: cmake
# autospec version: v19
# autospec commit: f35655a
#
# Source0 file verified with key 0xD7574483BB57B18D (jr@jriddell.org)
#
Name     : sddm-kcm
Version  : 6.1.5
Release  : 94
URL      : https://download.kde.org/stable/plasma/6.1.5/sddm-kcm-6.1.5.tar.xz
Source0  : https://download.kde.org/stable/plasma/6.1.5/sddm-kcm-6.1.5.tar.xz
Source1  : https://download.kde.org/stable/plasma/6.1.5/sddm-kcm-6.1.5.tar.xz.sig
Source2  : D7574483BB57B18D.pkey
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
BuildRequires : gnupg
BuildRequires : kcoreaddons-dev
BuildRequires : ki18n-dev
BuildRequires : kio-dev
BuildRequires : kservice-dev
BuildRequires : qt6base-dev
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

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
mkdir .gnupg
chmod 700 .gnupg
gpg --homedir .gnupg --import %{SOURCE2}
gpg --homedir .gnupg --status-fd 1 --verify %{SOURCE1} %{SOURCE0} > gpg.status
grep -E '^\[GNUPG:\] (GOODSIG|EXPKEYSIG) D7574483BB57B18D' gpg.status
%setup -q -n sddm-kcm-6.1.5
cd %{_builddir}/sddm-kcm-6.1.5
pushd ..
cp -a sddm-kcm-6.1.5 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1725988981
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export GOAMD64=v2
%cmake ..   -G 'Unix Makefiles'
make  %{?_smp_mflags}
popd
pushd ../buildavx2/
mkdir -p clr-build-avx2
pushd clr-build-avx2
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
GOAMD64=v3
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS -march=x86-64-v3 "
%cmake ..   -G 'Unix Makefiles'
make  %{?_smp_mflags}
popd
popd

%install
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export SOURCE_DATE_EPOCH=1725988981
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/sddm-kcm
cp %{_builddir}/sddm-kcm-%{version}/LICENSES/CC0-1.0.txt %{buildroot}/usr/share/package-licenses/sddm-kcm/82da472f6d00dc5f0a651f33ebb320aa9c7b08d0 || :
cp %{_builddir}/sddm-kcm-%{version}/LICENSES/GPL-2.0-or-later.txt %{buildroot}/usr/share/package-licenses/sddm-kcm/3e8971c6c5f16674958913a94a36b1ea7a00ac46 || :
cp %{_builddir}/sddm-kcm-%{version}/LICENSES/GPL-3.0-only.txt %{buildroot}/usr/share/package-licenses/sddm-kcm/e3bdbf20d43fc066a1b40a64d57d4ae5a31f177f || :
cp %{_builddir}/sddm-kcm-%{version}/LICENSES/LicenseRef-KDE-Accepted-GPL.txt %{buildroot}/usr/share/package-licenses/sddm-kcm/7d9831e05094ce723947d729c2a46a09d6e90275 || :
cp %{_builddir}/sddm-kcm-%{version}/LICENSES/LicenseRef-KDE-Accepted-GPL.txt %{buildroot}/usr/share/package-licenses/sddm-kcm/7d9831e05094ce723947d729c2a46a09d6e90275 || :
export GOAMD64=v2
pushd ../buildavx2/
GOAMD64=v3
pushd clr-build-avx2
%make_install_v3  || :
popd
popd
GOAMD64=v2
pushd clr-build
%make_install
popd
%find_lang kcm_sddm
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)
/V3/usr/lib64/libexec/kf6/kauth/kcmsddm_authhelper
/usr/lib64/libexec/kf6/kauth/kcmsddm_authhelper

%files bin
%defattr(-,root,root,-)
/V3/usr/bin/sddmthemeinstaller
/usr/bin/sddmthemeinstaller

%files data
%defattr(-,root,root,-)
/usr/share/applications/kcm_sddm.desktop
/usr/share/dbus-1/system-services/org.kde.kcontrol.kcmsddm.service
/usr/share/dbus-1/system.d/org.kde.kcontrol.kcmsddm.conf
/usr/share/knsrcfiles/sddmtheme.knsrc
/usr/share/polkit-1/actions/org.kde.kcontrol.kcmsddm.policy

%files lib
%defattr(-,root,root,-)
/V3/usr/lib64/qt6/plugins/plasma/kcms/systemsettings/kcm_sddm.so
/usr/lib64/qt6/plugins/plasma/kcms/systemsettings/kcm_sddm.so

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/sddm-kcm/3e8971c6c5f16674958913a94a36b1ea7a00ac46
/usr/share/package-licenses/sddm-kcm/7d9831e05094ce723947d729c2a46a09d6e90275
/usr/share/package-licenses/sddm-kcm/82da472f6d00dc5f0a651f33ebb320aa9c7b08d0
/usr/share/package-licenses/sddm-kcm/e3bdbf20d43fc066a1b40a64d57d4ae5a31f177f

%files locales -f kcm_sddm.lang
%defattr(-,root,root,-)

