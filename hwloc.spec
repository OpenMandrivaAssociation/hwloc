%define major 5
%define libname %mklibname %{name} %{major}
%define devname %mklibname %{name} -d

Summary:	Displays the hardware topology in convenient formats
Name:		hwloc
Version:	1.6.1
Release:	1
License:	BSD
Group:		System/Base
URL:		http://www.open-mpi.org/
Source0:	http://www.open-mpi.org/software/hwloc/v1.5/downloads/hwloc-%{version}.tar.bz2
BuildRequires:	numa-devel
BuildRequires:	pkgconfig(libxml-2.0)
BuildRequires:	pkgconfig(libpci)
BuildRequires:	pkgconfig(cairo)
BuildRequires:	pkgconfig(x11)
BuildRequires:	pkgconfig(ncursesw)
BuildRequires:	zlib-devel
# Not sure these are really needed for build:
BuildRequires:	pkgconfig(xdmcp)
BuildRequires:	pkgconfig(xau)
BuildRequires:	pkgconfig(xcb)
BuildRequires:	pkgconfig(xrender)
BuildRequires:	pkgconfig(freetype2)
BuildRequires:	pkgconfig(fontconfig)
BuildRequires:	pkgconfig(libpng)
BuildRequires:	pkgconfig(pixman-1)
BuildRequires:	bzip2-devel

%description
The Portable Hardware Locality (hwloc) software package provides a portable
abstraction (across OS, versions, architectures, ...) of the hierarchical
topology of modern architectures, including NUMA memory nodes, sockets, shared
caches, cores and simultaneous multithreading. It also gathers various system
attributes such as cache and memory information. It primarily aims at helping
applications with gathering information about modern computing hardware so as
to exploit it accordingly and efficiently.

%package -n %{libname}
Summary:	%{name} shared library
Group:		System/Libraries
Conflicts:	%{name} < 1.5

%description -n %{libname}
This package contains shared %{name} library.

%package -n %{devname}
Summary:	Header files, libraries and development documentation for %{name}
Group:		Development/Other
Requires:	%{libname} = %{version}-%{release}

%description -n %{devname}
This package contains the header files, static libraries and development
documentation for %{name}. If you like to develop programs using %{name},
you will need to install %{name}-devel.

%prep
%setup -q

%build
%configure2_5x
%make

%install
%makeinstall_std

%files
%doc AUTHORS COPYING NEWS README
%doc %{_mandir}/man1/hwloc-bind.1*
%doc %{_mandir}/man1/hwloc-calc.1*
%doc %{_mandir}/man1/hwloc-distrib.1*
%doc %{_mandir}/man1/hwloc-gather-topology.1*
%doc %{_mandir}/man1/hwloc-info.1*
%doc %{_mandir}/man1/hwloc-ls.1*
%doc %{_mandir}/man1/hwloc-ps.1*
%doc %{_mandir}/man1/lstopo.1*
%doc %{_mandir}/man1/lstopo-no-graphics.1*
%doc %{_mandir}/man7/hwloc.7*
%doc %{_mandir}/man1/hwloc-assembler.1*
%doc %{_mandir}/man1/hwloc-assembler-remote.1*
%doc %{_mandir}/man1/hwloc-distances.1*
%doc %{_mandir}/man1/hwloc-annotate.1*
%{_bindir}/hwloc-bind
%{_bindir}/hwloc-calc
%{_bindir}/hwloc-distrib
%{_bindir}/hwloc-gather-topology
%{_bindir}/hwloc-annotate
%{_bindir}/hwloc-info
%{_bindir}/hwloc-ls
%{_bindir}/hwloc-assembler
%{_bindir}/hwloc-assembler-remote
%{_bindir}/hwloc-distances
%{_bindir}/hwloc-ps
%{_bindir}/lstopo
%{_bindir}/lstopo-no-graphics
%{_datadir}/hwloc/

%files -n %{libname}
%{_libdir}/libhwloc.so.%{major}*

%files -n %{devname}
%doc %{_mandir}/man3/HWLOC_*.3*
%doc %{_mandir}/man3/hwloc_*.3*
%doc %{_mandir}/man3/hwlocality_*.3*
%{_includedir}/hwloc/
%{_includedir}/hwloc.h
%{_libdir}/libhwloc.so
%{_libdir}/pkgconfig/hwloc.pc


%changelog
* Tue Mar 06 2012 Alexander Khrukin <akhrukin@mandriva.org> 1.4.1-1
+ Revision: 782404
- version update  1.4.1
- la files removed

* Thu Jan 26 2012 Alexander Khrukin <akhrukin@mandriva.org> 1.4-1
+ Revision: 769199
- version update 1.4
- disable-static option removed cause it globally removed in 2012 rpm-policy

* Wed Dec 21 2011 Alexander Khrukin <akhrukin@mandriva.org> 1.3.1-1
+ Revision: 744135
- version update hwloc 1.3.1

* Sun Nov 20 2011 Alexander Khrukin <akhrukin@mandriva.org> 1.3-1
+ Revision: 732049
- dot removed
- spec fix in Group section
- imported package hwloc

