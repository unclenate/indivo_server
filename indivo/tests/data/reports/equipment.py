from indivo.tests.data.base import TestXMLDoc

_TEST_EQUIPMENT = [
    """
<Equipment xmlns='http://indivo.org/vocab/xml/documents#'>
  <dateStarted>2010-09-01</dateStarted>
  <name>Tractor</name> 
  <vendor>John Deer</vendor> 
  <description>Hello World</description>
</Equipment>
""",

    """
<Equipment xmlns="http://indivo.org/vocab/xml/documents#">
  <dateStarted>2010-09-02</dateStarted>
  <name>cane</name>
</Equipment>
"""
]

TEST_EQUIPMENT = [TestXMLDoc(raw_data) for raw_data in _TEST_EQUIPMENT]
