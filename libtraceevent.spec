#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : libtraceevent
Version  : 1.3.3
Release  : 5
URL      : https://git.kernel.org/pub/scm/libs/libtrace/libtraceevent.git/snapshot/libtraceevent-1.3.3.tar.gz
Source0  : https://git.kernel.org/pub/scm/libs/libtrace/libtraceevent.git/snapshot/libtraceevent-1.3.3.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : LGPL-2.0
Requires: libtraceevent-lib = %{version}-%{release}

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


%prep
%setup -q -n libtraceevent-1.3.3
cd %{_builddir}/libtraceevent-1.3.3

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1624657236
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
make  %{?_smp_mflags}


%install
export SOURCE_DATE_EPOCH=1624657236
rm -rf %{buildroot}
%make_install prefix=/usr libdir=/usr/lib64 install_lib
## install_append content
%make_install install_lib
## install_append end

%files
%defattr(-,root,root,-)

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
/usr/lib64/libtraceevent.so.1
/usr/lib64/libtraceevent.so.1.3.3
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
