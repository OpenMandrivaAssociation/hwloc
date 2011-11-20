Summary:	Displays the hardware topology in convenient formats
Name:		hwloc
Version:	1.3
Release:	1
License:	BSD
Group:		System/Base 
URL:		http://www.open-mpi.org/
Source:		http://www.open-mpi.org/software/hwloc/v1.3/downloads/hwloc-%{version}.tar.bz2

%description
The Portable Hardware Locality (hwloc) software package provides a portable
abstraction (across OS, versions, architectures, ...) of the hierarchical
topology of modern architectures, including NUMA memory nodes, sockets, shared
caches, cores and simultaneous multithreading. It also gathers various system
attributes such as cache and memory information. It primarily aims at helping
applications with gathering information about modern computing hardware so as
to exploit it accordingly and efficiently.

%package devel
Summary: Header files, libraries and development documentation for %{name}
Group: Development/Other
Requires: %{name} = %{version}-%{release}

%description devel
This package contains the header files, static libraries and development
documentation for %{name}. If you like to develop programs using %{name},
you will need to install %{name}-devel.

%prep
%setup -q

%build
%configure --disable-static
%make

%install
rm -rf %{buildroot}
%makeinstall_std

%files
%doc AUTHORS COPYING NEWS README
%doc %{_mandir}/man1/hwloc-bind.1*
%doc %{_mandir}/man1/hwloc-calc.1*
%doc %{_mandir}/man1/hwloc-distrib.1*
%doc %{_mandir}/man1/hwloc-gather-topology.1*
%doc %{_mandir}/man1/hwloc-info.1*
%doc %{_mandir}/man1/hwloc-ls.1*
%doc %{_mandir}/man1/hwloc-mask.1*
%doc %{_mandir}/man1/hwloc-ps.1*
%doc %{_mandir}/man1/lstopo.1*
%doc %{_mandir}/man7/hwloc.7*
%{_bindir}/hwloc-bind
%{_bindir}/hwloc-calc
%{_bindir}/hwloc-distrib
%{_bindir}/hwloc-gather-topology
%{_bindir}/hwloc-info
%{_bindir}/hwloc-ls
%{_bindir}/hwloc-mask
%{_bindir}/hwloc-ps
%{_bindir}/lstopo
%{_datadir}/hwloc/
%{_libdir}/libhwloc.so.*

%files devel
%defattr(-, root, root, 0755)
%doc %{_mandir}/man3/HWLOC_*.3*
%doc %{_mandir}/man3/hwloc_*.3*
%doc %{_mandir}/man3/hwlocality_*.3*
%{_includedir}/hwloc/
%{_includedir}/hwloc.h
%{_libdir}/libhwloc.so
%{_libdir}/*.la
%{_libdir}/pkgconfig/hwloc.pc
