%define url_ver %(echo %{version}|cut -d. -f1,2)

%define major 15
%define libname %mklibname %{name} %{major}
%define devname %mklibname %{name} -d

%define _disable_rebuild_configure 1

Summary:	Displays the hardware topology in convenient formats
Name:		hwloc
Version:	2.9.1
Release:	1
License:	BSD
Group:		System/Base
Url:		http://www.open-mpi.org/
Source0:	http://www.open-mpi.org/software/hwloc/v%{url_ver}/downloads/hwloc-%{version}.tar.bz2
BuildRequires:	bzip2-devel
%ifnarch %{armx} %{riscv}
BuildRequires:	numa-devel
%endif
BuildRequires:	pkgconfig(cairo)
BuildRequires:	pkgconfig(fontconfig)
BuildRequires:	pkgconfig(freetype2)
BuildRequires:	pkgconfig(libpng)
BuildRequires:	pkgconfig(libpci)
BuildRequires:	pkgconfig(libxml-2.0)
BuildRequires:	pkgconfig(ncursesw)
BuildRequires:	pkgconfig(pixman-1)
BuildRequires:	pkgconfig(x11)
BuildRequires:	pkgconfig(xau)
BuildRequires:	pkgconfig(xcb)
BuildRequires:	pkgconfig(xdmcp)
BuildRequires:	pkgconfig(xrender)
BuildRequires:	pkgconfig(zlib)

%description
The Portable Hardware Locality (hwloc) software package provides a portable
abstraction (across OS, versions, architectures, ...) of the hierarchical
topology of modern architectures, including NUMA memory nodes, sockets, shared
caches, cores and simultaneous multithreading. It also gathers various system
attributes such as cache and memory information. It primarily aims at helping
applications with gathering information about modern computing hardware so as
to exploit it accordingly and efficiently.

%files
%doc AUTHORS COPYING NEWS README
%doc %{_datadir}/doc/hwloc/dynamic_SVG_example.html
%{_mandir}/man1/hwloc-annotate.1*
%{_mandir}/man1/hwloc-bind.1*
%{_mandir}/man1/hwloc-calc.1*
%{_mandir}/man1/hwloc-compress-dir.1*
%{_mandir}/man1/hwloc-diff.1*
%{_mandir}/man1/hwloc-distrib.1*
%{_mandir}/man1/hwloc-gather-topology.1*
%{_mandir}/man1/hwloc-info.1*
%{_mandir}/man1/hwloc-ls.1*
%{_mandir}/man1/hwloc-patch.1*
%{_mandir}/man1/hwloc-ps.1*
%{_mandir}/man1/lstopo.1*
%{_mandir}/man1/lstopo-no-graphics.1*
%{_mandir}/man7/hwloc.7*
%ifnarch %{armx} %{riscv}
%{_mandir}/man1/hwloc-gather-cpuid.1.*
%{_mandir}/man1/hwloc-dump-hwdata.1.*
%{_bindir}/hwloc-dump-hwdata
%{_bindir}/hwloc-gather-cpuid
%endif
%{_bindir}/hwloc-annotate
%{_bindir}/hwloc-bind
%{_bindir}/hwloc-calc
%{_bindir}/hwloc-compress-dir
%{_bindir}/hwloc-diff
%{_bindir}/hwloc-distrib
%{_bindir}/hwloc-gather-topology
%{_bindir}/hwloc-info
%{_bindir}/hwloc-ls
%{_bindir}/hwloc-patch
%{_bindir}/hwloc-ps
%{_bindir}/lstopo
%{_bindir}/lstopo-no-graphics
%{_datadir}/hwloc/
%{_datadir}/applications/lstopo.desktop
%{_datadir}/bash-completion/completions/hwloc

#----------------------------------------------------------------------------

%package -n %{libname}
Summary:	%{name} shared library
Group:		System/Libraries
Conflicts:	%{name} < 1.5

%description -n %{libname}
This package contains shared %{name} library.

%files -n %{libname}
%{_libdir}/libhwloc.so.%{major}*

#----------------------------------------------------------------------------

%package -n %{devname}
Summary:	Header files, libraries and development documentation for %{name}
Group:		Development/Other
Requires:	%{libname} = %{EVRD}

%description -n %{devname}
This package contains the header files, static libraries and development
documentation for %{name}. If you like to develop programs using %{name},
you will need to install %{name}-devel.

%files -n %{devname}
%{_mandir}/man3/HWLOC_*.3*
%{_mandir}/man3/hwloc_*.3*
%{_mandir}/man3/hwlocality_*.3*
%{_datadir}/doc/hwloc/*.pdf
%{_includedir}/hwloc/
%{_includedir}/hwloc.h
%{_libdir}/libhwloc.so
%{_libdir}/pkgconfig/hwloc.pc

#----------------------------------------------------------------------------

%prep
%setup -q

%build
%configure
%make_build

%install
%make_install
