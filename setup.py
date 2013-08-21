# Copyright 2012 Hewlett-Packard Development Company, L.P.
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.

import setuptools

from jenkins_jobs.openstack.common import setup
from jenkins_jobs.version import version_info as version

requires = setup.parse_requirements()
test_requires = setup.parse_requirements(['tools/test-requires'])
depend_links = setup.parse_dependency_links()


setuptools.setup(
    name='jenkins-job-builder',
    version=version.canonical_version_string(always=True),
    author='Hewlett-Packard Development Company, L.P.',
    author_email='openstack@lists.launchpad.net',
    description='Manage Jenkins jobs with YAML',
    license='Apache License, Version 2.0',
    url='https://github.com/openstack-ci/jenkins-job-builder',
    packages=setuptools.find_packages(exclude=['tests', 'tests.*']),
    include_package_data=True,
    cmdclass=setup.get_cmdclass(),
    install_requires=requires,
    dependency_links=depend_links,
    zip_safe=False,
    classifiers=[
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Intended Audience :: Information Technology',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
        'Programming Language :: Python'
    ],
    entry_points={
        'console_scripts': [
            'jenkins-jobs=jenkins_jobs.cmd:main',
        ],
        'jenkins_jobs.projects': [
            'freestyle=jenkins_jobs.modules.project_freestyle:Freestyle',
            'maven=jenkins_jobs.modules.project_maven:Maven',
            'matrix=jenkins_jobs.modules.project_matrix:Matrix',
            'multijob=jenkins_jobs.modules.project_multijob:MultiJob',
        ],
        'jenkins_jobs.builders': [
            'shell=jenkins_jobs.modules.builders:shell',
            'ant=jenkins_jobs.modules.builders:ant',
            'trigger-builds=jenkins_jobs.modules.builders:trigger_builds',
            'builders-from=jenkins_jobs.modules.builders:builders_from',
            'inject=jenkins_jobs.modules.builders:inject',
            'artifact-resolver=jenkins_jobs.modules.builders:'
            'artifact_resolver',
            'copyartifact=jenkins_jobs.modules.builders:copyartifact',
            'gradle=jenkins_jobs.modules.builders:gradle',
            'batch=jenkins_jobs.modules.builders:batch',
            'maven-target=jenkins_jobs.modules.builders:maven_target',
            'multijob=jenkins_jobs.modules.builders:multijob',
            'grails=jenkins_jobs.modules.builders:grails',
            'conditional-step=jenkins_jobs.modules.builders:conditional_step',
            'msbuild=jenkins_jobs.modules.builders:msbuild',
        ],
        'jenkins_jobs.reporters': [
            'email=jenkins_jobs.modules.reporters:email',
        ],
        'jenkins_jobs.properties': [
            'promoted-build=jenkins_jobs.modules.properties:promoted_build',
            'github=jenkins_jobs.modules.properties:github',
            'throttle=jenkins_jobs.modules.properties:throttle',
            'inject=jenkins_jobs.modules.properties:inject',
            'authenticated-build=jenkins_jobs.modules.properties:'
            'authenticated_build',
            'authorization=jenkins_jobs.modules.properties:authorization',
            'extended-choice=jenkins_jobs.modules.properties:extended_choice',
            'priority-sorter=jenkins_jobs.modules.properties:priority_sorter',
        ],
        'jenkins_jobs.parameters': [
            'string=jenkins_jobs.modules.parameters:string_param',
            'password=jenkins_jobs.modules.parameters:password_param',
            'bool=jenkins_jobs.modules.parameters:bool_param',
            'file=jenkins_jobs.modules.parameters:file_param',
            'text=jenkins_jobs.modules.parameters:text_param',
            'label=jenkins_jobs.modules.parameters:label_param',
            'choice=jenkins_jobs.modules.parameters:choice_param',
            'validating-string=jenkins_jobs.modules.parameters:'
            'validating_string_param',
            'svn-tags=jenkins_jobs.modules.parameters:svn_tags_param',
        ],
        'jenkins_jobs.metadata': [
            'string=jenkins_jobs.modules.metadata:string_metadata',
            'number=jenkins_jobs.modules.metadata:number_metadata',
            'date=jenkins_jobs.modules.metadata:date_metadata',
        ],
        'jenkins_jobs.notifications': [
            'http=jenkins_jobs.modules.notifications:http_endpoint',
        ],
        'jenkins_jobs.publishers': [
            'archive=jenkins_jobs.modules.publishers:archive',
            'trigger-parameterized-builds='
            'jenkins_jobs.modules.publishers:trigger_parameterized_builds',
            'trigger=jenkins_jobs.modules.publishers:trigger',
            'coverage=jenkins_jobs.modules.publishers:coverage',
            'cobertura=jenkins_jobs.modules.publishers:cobertura',
            'ftp=jenkins_jobs.modules.publishers:ftp',
            'junit=jenkins_jobs.modules.publishers:junit',
            'xunit=jenkins_jobs.modules.publishers:xunit',
            'groovy-postbuild=jenkins_jobs.modules.publishers:'
            'groovy_postbuild',
            'violations=jenkins_jobs.modules.publishers:violations',
            'checkstyle=jenkins_jobs.modules.publishers:checkstyle',
            'scp=jenkins_jobs.modules.publishers:scp',
            'ssh=jenkins_jobs.modules.publishers:ssh',
            'pipeline=jenkins_jobs.modules.publishers:pipeline',
            'email=jenkins_jobs.modules.publishers:email',
            'claim-build=jenkins_jobs.modules.publishers:claim_build',
            'email-ext=jenkins_jobs.modules.publishers:email_ext',
            'fingerprint=jenkins_jobs.modules.publishers:fingerprint',
            'aggregate-tests=jenkins_jobs.modules.publishers:aggregate_tests',
            'cppcheck=jenkins_jobs.modules.publishers:cppcheck',
            'logparser=jenkins_jobs.modules.publishers:logparser',
            'copy-to-master=jenkins_jobs.modules.publishers:copy_to_master',
            'jira=jenkins_jobs.modules.publishers:jira',
            'cifs=jenkins_jobs.modules.publishers:cifs',
            'sonar=jenkins_jobs.modules.publishers:sonar',
            'performance=jenkins_jobs.modules.publishers:performance',
            'join-trigger=jenkins_jobs.modules.publishers:join_trigger',
            'jabber=jenkins_jobs.modules.publishers:jabber',
            'workspace-cleanup=jenkins_jobs.modules.publishers:'
            'workspace_cleanup',
            'maven-deploy=jenkins_jobs.modules.publishers:maven_deploy',
            'tap=jenkins_jobs.modules.publishers:tap',
            'text-finder=jenkins_jobs.modules.publishers:text_finder',
            'html-publisher=jenkins_jobs.modules.publishers:html_publisher',
            'post-tasks=jenkins_jobs.modules.publishers:post_tasks',
            'xml-summary=jenkins_jobs.modules.publishers:xml_summary',
            'robot=jenkins_jobs.modules.publishers:robot',
            'warnings=jenkins_jobs.modules.publishers:warnings',
        ],
        'jenkins_jobs.scm': [
            'git=jenkins_jobs.modules.scm:git',
            'svn=jenkins_jobs.modules.scm:svn',
            'tfs=jenkins_jobs.modules.scm:tfs',
        ],
        'jenkins_jobs.triggers': [
            'gerrit=jenkins_jobs.modules.triggers:gerrit',
            'pollscm=jenkins_jobs.modules.triggers:pollscm',
            'timed=jenkins_jobs.modules.triggers:timed',
            'github=jenkins_jobs.modules.triggers:github',
            'github-pull-request=jenkins_jobs.modules.triggers:'
            'github_pull_request',
        ],
        'jenkins_jobs.wrappers': [
            'timeout=jenkins_jobs.modules.wrappers:timeout',
            'timestamps=jenkins_jobs.modules.wrappers:timestamps',
            'ansicolor=jenkins_jobs.modules.wrappers:ansicolor',
            'mask-passwords=jenkins_jobs.modules.wrappers:mask_passwords',
            'build-name=jenkins_jobs.modules.wrappers:build_name',
            'workspace-cleanup=jenkins_jobs.modules.wrappers:'
            'workspace_cleanup',
            'port-allocator=jenkins_jobs.modules.wrappers:port_allocator',
            'locks=jenkins_jobs.modules.wrappers:locks',
            'copy-to-slave=jenkins_jobs.modules.wrappers:copy_to_slave',
            'inject=jenkins_jobs.modules.wrappers:inject',
            'env-file=jenkins_jobs.modules.wrappers:env_file',
            'jclouds=jenkins_jobs.modules.wrappers:jclouds',
            'build-user-vars=jenkins_jobs.modules.wrappers:build_user_vars',
            'release=jenkins_jobs.modules.wrappers:release',
            'sauce-ondemand=jenkins_jobs.modules.wrappers:sauce_ondemand',
            'rvm-env=jenkins_jobs.modules.wrappers:rvm_env',
            'pathignore=jenkins_jobs.modules.wrappers:pathignore',
            ('pre-scm-buildstep='
             'jenkins_jobs.modules.wrappers:pre_scm_buildstep'),
             'ansi-color=jenkins_jobs.modules.wrappers:ansi_color',
        ],
        'jenkins_jobs.modules': [
            'general=jenkins_jobs.modules.general:General',
            'builders=jenkins_jobs.modules.builders:Builders',
            'properties=jenkins_jobs.modules.properties:Properties',
            'parameters=jenkins_jobs.modules.parameters:Parameters',
            'metadata=jenkins_jobs.modules.metadata:Metadata',
            'notifications=jenkins_jobs.modules.notifications:Notifications',
            'publishers=jenkins_jobs.modules.publishers:Publishers',
            'reporters=jenkins_jobs.modules.reporters:Reporters',
            'scm=jenkins_jobs.modules.scm:SCM',
            'triggers=jenkins_jobs.modules.triggers:Triggers',
            'wrappers=jenkins_jobs.modules.wrappers:Wrappers',
            'zuul=jenkins_jobs.modules.zuul:Zuul',
            'hipchat=jenkins_jobs.modules.hipchat_notif:HipChat',
        ]
    }
)
