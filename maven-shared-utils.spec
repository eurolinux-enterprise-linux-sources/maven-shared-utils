Name:           maven-shared-utils
Version:        0.4
Release:        2%{?dist}
Summary:        Maven shared utility classes
License:        ASL 2.0
URL:            http://maven.apache.org/shared/maven-shared-utils
Source0:        http://repo1.maven.org/maven2/org/apache/maven/shared/%{name}/%{version}/%{name}-%{version}-source-release.zip
# Patching tests so that they are compatible with JUnit 4.11
# (upstream bug http://jira.codehaus.org/browse/MSHARED-285)
Patch0:         %{name}-tests.patch

BuildArch:      noarch

BuildRequires:  maven-local
BuildRequires:  apache-commons-lang3
BuildRequires:  apache-rat
BuildRequires:  maven-shared
BuildRequires:  maven-shade-plugin

%description
This project aims to be a functional replacement for plexus-utils in Maven.

It is not a 100% API compatible replacement though but a replacement with
improvements: lots of methods got cleaned up, generics got added and we dropped
a lot of unused code.

%package javadoc
Summary:        Javadoc for %{name}
    
%description javadoc
API documentation for %{name}.

%prep
%setup -q
%pom_remove_plugin org.codehaus.mojo:findbugs-maven-plugin
%patch0 -p1

%build
%mvn_build

%install
%mvn_install

%files -f .mfiles
%doc LICENSE NOTICE

%files javadoc -f .mfiles-javadoc
%doc LICENSE NOTICE

%changelog
* Fri Jun 28 2013 Mikolaj Izdebski <mizdebsk@redhat.com> - 0.4-2
- Rebuild to regenerate API documentation
- Resolves: CVE-2013-1571

* Mon Apr 22 2013 Tomas Radej <tradej@redhat.com> - 0.4-1
- Updated to latest upstream version
- Fixed and reenabled tests

* Mon Apr 08 2013 Michal Srb <msrb@redhat.com> - 0.3-2
- Disable tests (they don't work with junit >= 4.11)

* Fri Mar 15 2013 Michal Srb <msrb@redhat.com> - 0.3-1
- Update to upstream version 0.3

* Tue Feb 19 2013 Mikolaj Izdebski <mizdebsk@redhat.com> - 0.2-4
- Build with xmvn

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Feb 06 2013 Java SIG <java-devel@lists.fedoraproject.org> - 0.2-2
- Update for https://fedoraproject.org/wiki/Fedora_19_Maven_Rebuild
- Replace maven BuildRequires with maven-local

* Wed Jan 16 2013 Tomas Radej <tradej@redhat.com> - 0.2-1
- Initial version

