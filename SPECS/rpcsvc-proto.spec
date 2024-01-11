#
# spec file for package rpcsvc-proto
#
# Copyright (c) 2017 SUSE LINUX GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


Name:           rpcsvc-proto
Version:        1.4
Release:        9%{?dist}
Summary:        RPC protocol definitions
License:        BSD and LGPLv2+
Url:            https://github.com/thkukuk/rpcsvc-proto
Source0:        https://github.com/thkukuk/rpcsvc-proto/releases/v%{version}/%{name}-%{version}.tar.xz

Conflicts: glibc-headers < 2.26.9000-36
Conflicts: glibc-common < 2.26.9000-36

BuildRequires: make
BuildRequires:  gcc
BuildRequires: automake, autoconf

%description
The rpcsvc-proto package includes several rpcsvc header files
and RPC protocol definitions from SunRPC sources (as shipped with
glibc).

%package devel
Summary:        RPC protocol definitions

%description devel
The rpcsvc-proto package includes several rpcsvc header files
and RPC protocol definitions from SunRPC sources (as shipped with
glibc).

%package -n rpcgen
Summary:        RPC protocol compiler
Provides:       rpcgen

%description -n rpcgen
rpcgen is a tool that generates C code to implement an RPC protocol.
The input to rpcgen is a language similar to C known as RPC Language
(Remote Procedure Call Language).

%prep
%autosetup -p 1

%build
%configure
%make_build

%install
%make_install

# rquota.x and rquota.h are provided by quota
rm -f $RPM_BUILD_ROOT%{_prefix}/include/rpcsvc/rquota.[hx]

%files devel
%license COPYING
%{_includedir}/rpcsvc/

%files -n rpcgen
%{_bindir}/rpcgen
%{_mandir}/man1/rpcgen.1*

%changelog
* Tue Aug 10 2021 Mohan Boddu <mboddu@redhat.com> - 1.4-9
- Rebuilt for IMA sigs, glibc 2.34, aarch64 flags
  Related: rhbz#1991688

* Fri Apr 16 2021 Mohan Boddu <mboddu@redhat.com> - 1.4-8
- Rebuilt for RHEL 9 BETA on Apr 15th 2021. Related: rhbz#1947937

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-6
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue May 29 2018 Steve Dickson <steved@redhat.com>  1.4-0
- Updated to the latest upstream release: v1.4 (bz 1559181)

* Tue Mar 27 2018 Björn Esser <besser82@fedoraproject.org> - 1.3.1-4
- Enable MT code as libtirpc supports it

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Jan 23 2018 Steve Dickson <steved@redhat.com>  1.3.1-2
- Remove rquota.[hx] headers which are provided by quota (bz 1537133)

* Wed Jan  17 2018 Steve Dickson <steved@redhat.com>  1.3.1-1
- Initial commit (bz 1532364)
