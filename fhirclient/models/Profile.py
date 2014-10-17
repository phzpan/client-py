#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 0.0.82.2943 (profile.profile.json) on 2014-10-17.
#  2014, SMART Platforms.

# We need to support importing other generated classes without relying on the
# models being part of a specific module. To do so we prepend the current
# directory sys.path - better solutions are welcome!
import sys
import os.path
abspath = os.path.abspath(os.path.dirname(__file__))
if abspath not in sys.path:
    sys.path.insert(0, abspath)


import coding
import contact
import fhirdate
import fhirelement
import fhirreference
import fhirresource
import narrative
import valueset


class Profile(fhirresource.FHIRResource):
    """ Resource Profile.
    
    Scope and Usage This specification describes a set of base resources that
    are used in many different contexts in healthcare. In order to make this
    manageable, applications and specifications need to be able to describe
    restrictions on how one or more resource(s) are used, including defining
    extensions, and controlling how terminology is used. These descriptions
    need to be able to be shared through repositories of profile definitions,
    and need to allow for these usage statements to be published, compared, and
    used as the basis for code, report and UI generation. All these things are
    done using a "Profile", which itself is represented as a resource.
    
    Profile resources have three main parts:
    
    * A metadata section the describes the profile, and supports registry
    searching
    * Structures that define and describe how a Resource or Data Type is used
    * Extension Definitions that define extensions that can be used in
    structures
    This page defines the profile resource, and describes how it is used. Note
    that as part of the specification itself, a full set of profiles for all
    resources and data types is published.
    
    A FHIR RESTful server serving the profile resource is also a profile
    repository. HL7 hosts one for public registration of FHIR profiles at (yet
    to be done).
    """
    
    resource_name = "Profile"
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        self.code = None
        """ Assist with indexing and finding.
        List of `Coding` items (represented as `dict` in JSON). """
        
        self.date = None
        """ Date for this version of the profile.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.description = None
        """ Natural language description of the profile.
        Type `str`. """
        
        self.experimental = False
        """ If for testing purposes, not real usage.
        Type `bool`. """
        
        self.extensionDefn = None
        """ Definition of an extension.
        List of `ProfileExtensionDefn` items (represented as `dict` in JSON). """
        
        self.fhirVersion = None
        """ FHIR Version this profile targets.
        Type `str`. """
        
        self.identifier = None
        """ Logical id to reference this profile.
        Type `str`. """
        
        self.mapping = None
        """ External specification that the content is mapped to.
        List of `ProfileMapping` items (represented as `dict` in JSON). """
        
        self.name = None
        """ Informal name for this profile.
        Type `str`. """
        
        self.publisher = None
        """ Name of the publisher (Organization or individual).
        Type `str`. """
        
        self.query = None
        """ Definition of a named query.
        List of `ProfileQuery` items (represented as `dict` in JSON). """
        
        self.requirements = None
        """ Scope and Usage this profile is for.
        Type `str`. """
        
        self.status = None
        """ draft | active | retired.
        Type `str`. """
        
        self.structure = None
        """ A constraint on a resource or a data type.
        List of `ProfileStructure` items (represented as `dict` in JSON). """
        
        self.telecom = None
        """ Contact information of the publisher.
        List of `Contact` items (represented as `dict` in JSON). """
        
        self.text = None
        """ Text summary of the resource, for human interpretation.
        Type `Narrative` (represented as `dict` in JSON). """
        
        self.version = None
        """ Logical id for this version of the profile.
        Type `str`. """
        
        super(Profile, self).__init__(jsondict)
    
    def update_with_json(self, jsondict):
        super(Profile, self).update_with_json(jsondict)
        if 'code' in jsondict:
            self.code = coding.Coding.with_json(jsondict['code'])
        if 'date' in jsondict:
            self.date = fhirdate.FHIRDate.with_json(jsondict['date'])
        if 'description' in jsondict:
            self.description = jsondict['description']
        if 'experimental' in jsondict:
            self.experimental = jsondict['experimental']
        if 'extensionDefn' in jsondict:
            self.extensionDefn = ProfileExtensionDefn.with_json(jsondict['extensionDefn'])
        if 'fhirVersion' in jsondict:
            self.fhirVersion = jsondict['fhirVersion']
        if 'identifier' in jsondict:
            self.identifier = jsondict['identifier']
        if 'mapping' in jsondict:
            self.mapping = ProfileMapping.with_json(jsondict['mapping'])
        if 'name' in jsondict:
            self.name = jsondict['name']
        if 'publisher' in jsondict:
            self.publisher = jsondict['publisher']
        if 'query' in jsondict:
            self.query = ProfileQuery.with_json(jsondict['query'])
        if 'requirements' in jsondict:
            self.requirements = jsondict['requirements']
        if 'status' in jsondict:
            self.status = jsondict['status']
        if 'structure' in jsondict:
            self.structure = ProfileStructure.with_json(jsondict['structure'])
        if 'telecom' in jsondict:
            self.telecom = contact.Contact.with_json(jsondict['telecom'])
        if 'text' in jsondict:
            self.text = narrative.Narrative.with_json(jsondict['text'])
        if 'version' in jsondict:
            self.version = jsondict['version']


class ProfileMapping(fhirelement.FHIRElement):
    """ External specification that the content is mapped to.
    
    An external specification that the content is mapped to.
    """
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        self.comments = None
        """ Versions, Issues, Scope limitations etc.
        Type `str`. """
        
        self.identity = None
        """ Internal id when this mapping is used.
        Type `str`. """
        
        self.name = None
        """ Names what this mapping refers to.
        Type `str`. """
        
        self.uri = None
        """ Identifies what this mapping refers to.
        Type `str`. """
        
        super(ProfileMapping, self).__init__(jsondict)
    
    def update_with_json(self, jsondict):
        super(ProfileMapping, self).update_with_json(jsondict)
        if 'comments' in jsondict:
            self.comments = jsondict['comments']
        if 'identity' in jsondict:
            self.identity = jsondict['identity']
        if 'name' in jsondict:
            self.name = jsondict['name']
        if 'uri' in jsondict:
            self.uri = jsondict['uri']


class ProfileStructure(fhirelement.FHIRElement):
    """ A constraint on a resource or a data type.
    
    A constraint statement about what contents a resource or data type may
    have.
    """
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        self.element = None
        """ Definition of elements in the resource (if no profile).
        List of `ProfileStructureElement` items (represented as `dict` in JSON). """
        
        self.name = None
        """ Name for this particular structure (reference target).
        Type `str`. """
        
        self.publish = False
        """ This definition is published (i.e. for validation).
        Type `bool`. """
        
        self.purpose = None
        """ Human summary: why describe this resource?.
        Type `str`. """
        
        self.searchParam = None
        """ Search params defined.
        List of `ProfileStructureSearchParam` items (represented as `dict` in JSON). """
        
        self.type = None
        """ The Resource or Data Type being described.
        Type `str`. """
        
        super(ProfileStructure, self).__init__(jsondict)
    
    def update_with_json(self, jsondict):
        super(ProfileStructure, self).update_with_json(jsondict)
        if 'element' in jsondict:
            self.element = ProfileStructureElement.with_json(jsondict['element'])
        if 'name' in jsondict:
            self.name = jsondict['name']
        if 'publish' in jsondict:
            self.publish = jsondict['publish']
        if 'purpose' in jsondict:
            self.purpose = jsondict['purpose']
        if 'searchParam' in jsondict:
            self.searchParam = ProfileStructureSearchParam.with_json(jsondict['searchParam'])
        if 'type' in jsondict:
            self.type = jsondict['type']


class ProfileStructureElement(fhirelement.FHIRElement):
    """ Definition of elements in the resource (if no profile).
    
    Captures constraints on each element within the resource.
    """
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        self.definition = None
        """ More specific definition of the element.
        Type `ProfileStructureElementDefinition` (represented as `dict` in JSON). """
        
        self.name = None
        """ Name for this particular element definition (reference target).
        Type `str`. """
        
        self.path = None
        """ The path of the element (see the formal definitions).
        Type `str`. """
        
        self.representation = None
        """ How this element is represented in instances.
        List of `str` items. """
        
        self.slicing = None
        """ This element is sliced - slices follow.
        Type `ProfileStructureElementSlicing` (represented as `dict` in JSON). """
        
        super(ProfileStructureElement, self).__init__(jsondict)
    
    def update_with_json(self, jsondict):
        super(ProfileStructureElement, self).update_with_json(jsondict)
        if 'definition' in jsondict:
            self.definition = ProfileStructureElementDefinition.with_json(jsondict['definition'])
        if 'name' in jsondict:
            self.name = jsondict['name']
        if 'path' in jsondict:
            self.path = jsondict['path']
        if 'representation' in jsondict:
            self.representation = jsondict['representation']
        if 'slicing' in jsondict:
            self.slicing = ProfileStructureElementSlicing.with_json(jsondict['slicing'])


class ProfileStructureElementSlicing(fhirelement.FHIRElement):
    """ This element is sliced - slices follow.
    
    Indicates that the element is sliced into a set of alternative definitions
    (there are multiple definitions on a single element in the base resource).
    The set of slices is any elements that come after this in the element
    sequence that have the same path, until a shorter path occurs (the shorter
    path terminates the set).
    """
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        self.discriminator = None
        """ Element that used to distinguish the slices.
        Type `str`. """
        
        self.ordered = False
        """ If elements must be in same order as slices.
        Type `bool`. """
        
        self.rules = None
        """ closed | open | openAtEnd.
        Type `str`. """
        
        super(ProfileStructureElementSlicing, self).__init__(jsondict)
    
    def update_with_json(self, jsondict):
        super(ProfileStructureElementSlicing, self).update_with_json(jsondict)
        if 'discriminator' in jsondict:
            self.discriminator = jsondict['discriminator']
        if 'ordered' in jsondict:
            self.ordered = jsondict['ordered']
        if 'rules' in jsondict:
            self.rules = jsondict['rules']


class ProfileStructureElementDefinition(fhirelement.FHIRElement):
    """ More specific definition of the element.
    
    Definition of the content of the element to provide a more specific
    definition than that contained for the element in the base resource.
    """
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        self.binding = None
        """ ValueSet details if this is coded.
        Type `ProfileStructureElementDefinitionBinding` (represented as `dict` in JSON). """
        
        self.comments = None
        """ Comments about the use of this element.
        Type `str`. """
        
        self.condition = None
        """ Reference to invariant about presence.
        List of `str` items. """
        
        self.constraint = None
        """ Condition that must evaluate to true.
        List of `ProfileStructureElementDefinitionConstraint` items (represented as `dict` in JSON). """
        
        self.example = None
        """ Example value: [as defined for type].
        Type `FHIRElement` (represented as `dict` in JSON). """
        
        self.formal = None
        """ Full formal definition in human language.
        Type `str`. """
        
        self.isModifier = False
        """ If this modifies the meaning of other elements.
        Type `bool`. """
        
        self.mapping = None
        """ Map element to another set of definitions.
        List of `ProfileStructureElementDefinitionMapping` items (represented as `dict` in JSON). """
        
        self.max = None
        """ Maximum Cardinality (a number or *).
        Type `str`. """
        
        self.maxLength = None
        """ Length for strings.
        Type `int`. """
        
        self.min = None
        """ Minimum Cardinality.
        Type `int`. """
        
        self.mustSupport = False
        """ If the element must supported.
        Type `bool`. """
        
        self.nameReference = None
        """ To another element constraint (by element.name).
        Type `str`. """
        
        self.requirements = None
        """ Why is this needed?.
        Type `str`. """
        
        self.short = None
        """ Concise definition for xml presentation.
        Type `str`. """
        
        self.synonym = None
        """ Other names.
        List of `str` items. """
        
        self.type = None
        """ Data type and Profile for this element.
        List of `ProfileStructureElementDefinitionType` items (represented as `dict` in JSON). """
        
        self.value = None
        """ Fixed value: [as defined for a primitive type].
        Type `FHIRElement` (represented as `dict` in JSON). """
        
        super(ProfileStructureElementDefinition, self).__init__(jsondict)
    
    def update_with_json(self, jsondict):
        super(ProfileStructureElementDefinition, self).update_with_json(jsondict)
        if 'binding' in jsondict:
            self.binding = ProfileStructureElementDefinitionBinding.with_json(jsondict['binding'])
        if 'comments' in jsondict:
            self.comments = jsondict['comments']
        if 'condition' in jsondict:
            self.condition = jsondict['condition']
        if 'constraint' in jsondict:
            self.constraint = ProfileStructureElementDefinitionConstraint.with_json(jsondict['constraint'])
        if 'example' in jsondict:
            self.example = fhirelement.FHIRElement.with_json(jsondict['example'])
        if 'formal' in jsondict:
            self.formal = jsondict['formal']
        if 'isModifier' in jsondict:
            self.isModifier = jsondict['isModifier']
        if 'mapping' in jsondict:
            self.mapping = ProfileStructureElementDefinitionMapping.with_json(jsondict['mapping'])
        if 'max' in jsondict:
            self.max = jsondict['max']
        if 'maxLength' in jsondict:
            self.maxLength = jsondict['maxLength']
        if 'min' in jsondict:
            self.min = jsondict['min']
        if 'mustSupport' in jsondict:
            self.mustSupport = jsondict['mustSupport']
        if 'nameReference' in jsondict:
            self.nameReference = jsondict['nameReference']
        if 'requirements' in jsondict:
            self.requirements = jsondict['requirements']
        if 'short' in jsondict:
            self.short = jsondict['short']
        if 'synonym' in jsondict:
            self.synonym = jsondict['synonym']
        if 'type' in jsondict:
            self.type = ProfileStructureElementDefinitionType.with_json(jsondict['type'])
        if 'value' in jsondict:
            self.value = fhirelement.FHIRElement.with_json(jsondict['value'])


class ProfileStructureElementDefinitionType(fhirelement.FHIRElement):
    """ Data type and Profile for this element.
    
    The data type or resource that the value of this element is permitted to
    be.
    """
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        self.aggregation = None
        """ contained | referenced | bundled - how aggregated.
        List of `str` items. """
        
        self.code = None
        """ Name of Data type or Resource.
        Type `str`. """
        
        self.profile = None
        """ Profile.structure to apply.
        Type `str`. """
        
        super(ProfileStructureElementDefinitionType, self).__init__(jsondict)
    
    def update_with_json(self, jsondict):
        super(ProfileStructureElementDefinitionType, self).update_with_json(jsondict)
        if 'aggregation' in jsondict:
            self.aggregation = jsondict['aggregation']
        if 'code' in jsondict:
            self.code = jsondict['code']
        if 'profile' in jsondict:
            self.profile = jsondict['profile']


class ProfileStructureElementDefinitionConstraint(fhirelement.FHIRElement):
    """ Condition that must evaluate to true.
    
    Formal constraints such as co-occurrence and other constraints that can be
    computationally evaluated within the context of the instance.
    """
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        self.human = None
        """ Human description of constraint.
        Type `str`. """
        
        self.key = None
        """ Target of 'condition' reference above.
        Type `str`. """
        
        self.name = None
        """ Short human label.
        Type `str`. """
        
        self.severity = None
        """ error | warning.
        Type `str`. """
        
        self.xpath = None
        """ XPath expression of constraint.
        Type `str`. """
        
        super(ProfileStructureElementDefinitionConstraint, self).__init__(jsondict)
    
    def update_with_json(self, jsondict):
        super(ProfileStructureElementDefinitionConstraint, self).update_with_json(jsondict)
        if 'human' in jsondict:
            self.human = jsondict['human']
        if 'key' in jsondict:
            self.key = jsondict['key']
        if 'name' in jsondict:
            self.name = jsondict['name']
        if 'severity' in jsondict:
            self.severity = jsondict['severity']
        if 'xpath' in jsondict:
            self.xpath = jsondict['xpath']


class ProfileStructureElementDefinitionBinding(fhirelement.FHIRElement):
    """ ValueSet details if this is coded.
    
    Binds to a value set if this element is coded (code, Coding,
    CodeableConcept).
    """
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        self.conformance = None
        """ required | preferred | example.
        Type `str`. """
        
        self.description = None
        """ Human explanation of the value set.
        Type `str`. """
        
        self.isExtensible = False
        """ Can additional codes be used?.
        Type `bool`. """
        
        self.name = None
        """ Descriptive Name.
        Type `str`. """
        
        self.referenceResource = None
        """ Source of value set.
        Type `FHIRReference` referencing `ValueSet` (represented as `dict` in JSON). """
        
        self.referenceUri = None
        """ Source of value set.
        Type `str`. """
        
        super(ProfileStructureElementDefinitionBinding, self).__init__(jsondict)
    
    def update_with_json(self, jsondict):
        super(ProfileStructureElementDefinitionBinding, self).update_with_json(jsondict)
        if 'conformance' in jsondict:
            self.conformance = jsondict['conformance']
        if 'description' in jsondict:
            self.description = jsondict['description']
        if 'isExtensible' in jsondict:
            self.isExtensible = jsondict['isExtensible']
        if 'name' in jsondict:
            self.name = jsondict['name']
        if 'referenceResource' in jsondict:
            self.referenceResource = fhirreference.FHIRReference.with_json_and_owner(jsondict['referenceResource'], self, valueset.ValueSet)
        if 'referenceUri' in jsondict:
            self.referenceUri = jsondict['referenceUri']


class ProfileStructureElementDefinitionMapping(fhirelement.FHIRElement):
    """ Map element to another set of definitions.
    
    Identifies a concept from an external specification that roughly
    corresponds to this element.
    """
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        self.identity = None
        """ Reference to mapping declaration.
        Type `str`. """
        
        self.map = None
        """ Details of the mapping.
        Type `str`. """
        
        super(ProfileStructureElementDefinitionMapping, self).__init__(jsondict)
    
    def update_with_json(self, jsondict):
        super(ProfileStructureElementDefinitionMapping, self).update_with_json(jsondict)
        if 'identity' in jsondict:
            self.identity = jsondict['identity']
        if 'map' in jsondict:
            self.map = jsondict['map']


class ProfileStructureSearchParam(fhirelement.FHIRElement):
    """ Search params defined.
    
    Additional search parameters for implementations to support and/or make use
    of.
    """
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        self.documentation = None
        """ Contents and meaning of search parameter.
        Type `str`. """
        
        self.name = None
        """ Name of search parameter.
        Type `str`. """
        
        self.target = None
        """ Types of resource (if a resource reference).
        List of `str` items. """
        
        self.type = None
        """ number | date | string | token | reference | composite | quantity.
        Type `str`. """
        
        self.xpath = None
        """ XPath that extracts the parameter set.
        Type `str`. """
        
        super(ProfileStructureSearchParam, self).__init__(jsondict)
    
    def update_with_json(self, jsondict):
        super(ProfileStructureSearchParam, self).update_with_json(jsondict)
        if 'documentation' in jsondict:
            self.documentation = jsondict['documentation']
        if 'name' in jsondict:
            self.name = jsondict['name']
        if 'target' in jsondict:
            self.target = jsondict['target']
        if 'type' in jsondict:
            self.type = jsondict['type']
        if 'xpath' in jsondict:
            self.xpath = jsondict['xpath']


class ProfileExtensionDefn(fhirelement.FHIRElement):
    """ Definition of an extension.
    
    An extension defined as part of the profile.
    """
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        self.code = None
        """ Identifies the extension in this profile.
        Type `str`. """
        
        self.context = None
        """ Where the extension can be used in instances.
        List of `str` items. """
        
        self.contextType = None
        """ resource | datatype | mapping | extension.
        Type `str`. """
        
        self.definition = None
        """ Definition of the extension and its content.
        Type `ProfileExtensionDefnDefinition` (represented as `dict` in JSON). """
        
        self.display = None
        """ Use this name when displaying the value.
        Type `str`. """
        
        super(ProfileExtensionDefn, self).__init__(jsondict)
    
    def update_with_json(self, jsondict):
        super(ProfileExtensionDefn, self).update_with_json(jsondict)
        if 'code' in jsondict:
            self.code = jsondict['code']
        if 'context' in jsondict:
            self.context = jsondict['context']
        if 'contextType' in jsondict:
            self.contextType = jsondict['contextType']
        if 'definition' in jsondict:
            self.definition = ProfileExtensionDefnDefinition.with_json(jsondict['definition'])
        if 'display' in jsondict:
            self.display = jsondict['display']


class ProfileExtensionDefnDefinition(fhirelement.FHIRElement):
    """ Definition of the extension and its content.
    """
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        super(ProfileExtensionDefnDefinition, self).__init__(jsondict)


class ProfileQuery(fhirelement.FHIRElement):
    """ Definition of a named query.
    
    Definition of a named query and its parameters and their meaning.
    """
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        self.documentation = None
        """ Describes the named query.
        Type `str`. """
        
        self.name = None
        """ Special named queries (_query=).
        Type `str`. """
        
        self.parameter = None
        """ Parameter for the named query.
        List of `ProfileQueryParameter` items (represented as `dict` in JSON). """
        
        super(ProfileQuery, self).__init__(jsondict)
    
    def update_with_json(self, jsondict):
        super(ProfileQuery, self).update_with_json(jsondict)
        if 'documentation' in jsondict:
            self.documentation = jsondict['documentation']
        if 'name' in jsondict:
            self.name = jsondict['name']
        if 'parameter' in jsondict:
            self.parameter = ProfileQueryParameter.with_json(jsondict['parameter'])


class ProfileQueryParameter(fhirelement.FHIRElement):
    """ Parameter for the named query.
    
    A parameter of a named query.
    """
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        super(ProfileQueryParameter, self).__init__(jsondict)

