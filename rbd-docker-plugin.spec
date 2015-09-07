# SRC https://github.com/yp-engineering/rbd-docker-plugin/archive/0.1.9.tar.gz

%define version 0.1.9
%{!?release: %{!?release: %define release 1}}

Summary: Ceph RBD docker volume driver plugin.
Name: rbd-docker-plugin
Version: %{version}
Release: %{release}%{?dist}
License: MIT
Group: misc
URL: https://github.com/yp-engineering/rbd-docker-plugin/
Source0: https://github.com/yp-engineering/rbd-docker-plugin/archive/%{version}.tar.gz
Source1: rbd-docker-plugin.service
BuildArch: x86_64
BuildRoot: %{_tmppath}/%{name}-%{version}
BuildRequires: golang >= 1.4.0, make, librados2-devel >= 0.94.0, librbd1-devel >= 0.94.0

Requires: ceph >= 0.94.0, docker-engine >= 1.8.0

%description
Ceph RBD docker volume driver plugin.

%prep
%setup -q -n %{name}-%{version}

%build
export GOPATH=%{_builddir}/go
mkdir -p ${GOPATH}
export GOBIN=${GOPATH}/bin
mkdir -p ${GOBIN}
go get
make

%install
install -d %{buildroot}%{_bindir}
install -d %{buildroot}%{_unitdir}
install -p -m 755 dist/%{name} %{buildroot}%{_bindir}/%{name}
install -p -D -m 755 %{S:1} %{buildroot}%{_unitdir}/

%files
%defattr(-,root,root)
%{_unitdir}/rbd-docker-plugin.service
%{_bindir}/%{name}

%post
%systemd_post rbd-docker-plugin.service

%preun
%systemd_preun rbd-docker-plugin.service

%postun
# When the last version of a package is erased, $1 is 0
# Otherwise it's an upgrade and we need to restart the service
if [ $1 -ge 1 ]; then
    /usr/bin/systemctl restart rbd-docker-plugin.service
fi
/usr/bin/systemctl daemon-reload >/dev/null 2>&1 || true

%changelog
* Mon Sep  7 sheepkiller
- Initial version
