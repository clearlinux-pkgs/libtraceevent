#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: meson
# autospec version: v17
# autospec commit: b5caddc
#
Name     : libtraceevent
Version  : 1.8.3
Release  : 25
URL      : https://git.kernel.org/pub/scm/libs/libtrace/libtraceevent.git/snapshot/libtraceevent-1.8.3.tar.gz
Source0  : https://git.kernel.org/pub/scm/libs/libtrace/libtraceevent.git/snapshot/libtraceevent-1.8.3.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : LGPL-2.0
Requires: libtraceevent-lib = %{version}-%{release}
BuildRequires : asciidoc
BuildRequires : buildreq-meson
BuildRequires : pkgconfig(cunit)
BuildRequires : xmlto
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
The official repository is here:
https://git.kernel.org/pub/scm/libs/libtrace/libtraceevent.git/

%package dev
Summary: dev components for the libtraceevent package.
Group: Development
Requires: libtraceevent-lib = %{version}-%{release}
Provides: libtraceevent-devel = %{version}-%{release}
Requires: libtraceevent = %{version}-%{release}

%description dev
dev components for the libtraceevent package.


%package lib
Summary: lib components for the libtraceevent package.
Group: Libraries

%description lib
lib components for the libtraceevent package.


%package staticdev
Summary: staticdev components for the libtraceevent package.
Group: Default
Requires: libtraceevent-dev = %{version}-%{release}

%description staticdev
staticdev components for the libtraceevent package.


%prep
%setup -q -n libtraceevent-1.8.3
cd %{_builddir}/libtraceevent-1.8.3
pushd ..
cp -a libtraceevent-1.8.3 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1721919798
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
meson --libdir=lib64 --prefix=/usr --buildtype=plain   builddir
ninja -v -C builddir
GOAMD64=v3
CFLAGS="$CFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 " CXXFLAGS="$CXXFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 " LDFLAGS="$LDFLAGS -march=x86-64-v3 " meson --libdir=lib64 --prefix=/usr --buildtype=plain   builddiravx2
ninja -v -C builddiravx2

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
meson test -C builddir --print-errorlogs
cd ../buildavx2;
meson test -C builddir --print-errorlogs || :

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
export GOAMD64=v2
GOAMD64=v3
DESTDIR=%{buildroot}-v3 ninja -C builddiravx2 install
GOAMD64=v2
DESTDIR=%{buildroot} ninja -C builddir install
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)
/usr/lib64/traceevent/plugins/libtraceevent-dynamic-list

%files dev
%defattr(-,root,root,-)
/usr/include/traceevent/event-parse.h
/usr/include/traceevent/event-utils.h
/usr/include/traceevent/kbuffer.h
/usr/include/traceevent/trace-seq.h
/usr/lib64/libtraceevent.so
/usr/lib64/pkgconfig/libtraceevent.pc

%files lib
%defattr(-,root,root,-)
/V3/usr/lib64/libtraceevent.so.1.8.3
/V3/usr/lib64/traceevent/plugins/plugin_cfg80211.so
/V3/usr/lib64/traceevent/plugins/plugin_function.so
/V3/usr/lib64/traceevent/plugins/plugin_futex.so
/V3/usr/lib64/traceevent/plugins/plugin_hrtimer.so
/V3/usr/lib64/traceevent/plugins/plugin_jbd2.so
/V3/usr/lib64/traceevent/plugins/plugin_kmem.so
/V3/usr/lib64/traceevent/plugins/plugin_kvm.so
/V3/usr/lib64/traceevent/plugins/plugin_mac80211.so
/V3/usr/lib64/traceevent/plugins/plugin_sched_switch.so
/V3/usr/lib64/traceevent/plugins/plugin_scsi.so
/V3/usr/lib64/traceevent/plugins/plugin_tlb.so
/V3/usr/lib64/traceevent/plugins/plugin_xen.so
/usr/lib64/libtraceevent.so.1
/usr/lib64/libtraceevent.so.1.8.3
/usr/lib64/traceevent/plugins/plugin_cfg80211.so
/usr/lib64/traceevent/plugins/plugin_function.so
/usr/lib64/traceevent/plugins/plugin_futex.so
/usr/lib64/traceevent/plugins/plugin_hrtimer.so
/usr/lib64/traceevent/plugins/plugin_jbd2.so
/usr/lib64/traceevent/plugins/plugin_kmem.so
/usr/lib64/traceevent/plugins/plugin_kvm.so
/usr/lib64/traceevent/plugins/plugin_mac80211.so
/usr/lib64/traceevent/plugins/plugin_sched_switch.so
/usr/lib64/traceevent/plugins/plugin_scsi.so
/usr/lib64/traceevent/plugins/plugin_tlb.so
/usr/lib64/traceevent/plugins/plugin_xen.so

%files staticdev
%defattr(-,root,root,-)
/usr/lib64/libtraceevent.a
