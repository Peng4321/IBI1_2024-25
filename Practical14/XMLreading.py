# XMLreading_DOM.py
from xml.dom.minidom import parse
from datetime import datetime
start = datetime.now()
result = {
    "biological_process": ("", "", 0),
    "molecular_function": ("", "", 0),
    "cellular_component": ("", "", 0)
}
try:
    doc = parse("go_obo.xml")
    terms = doc.getElementsByTagName("term")
    print(f"Total terms found: {len(terms)}\n")
    for term in terms:
        try:
            ns_list = term.getElementsByTagName("namespace")
            name_list = term.getElementsByTagName("name")
            id_list = term.getElementsByTagName("id")
            isas = term.getElementsByTagName("is_a")

            if not (ns_list and name_list and id_list):
                continue  
            #considering there are more than one that meet the condition
            ns = ns_list[0].firstChild.nodeValue.strip()
            name = [name_list[0].firstChild.nodeValue.strip()]
            id_ = [id_list[0].firstChild.nodeValue.strip()]
            if ns in result and len(isas) >= result[ns][2]:
                name = name.append(name_list[0].firstChild.nodeValue.strip())    
                id_ = id_.append(id_list[0].firstChild.nodeValue.strip())

        except Exception as inner_e:
            print("Error parsing a <term>:", inner_e)
            continue
except Exception as e:
    print("Failed to parse XML:", e)
    exit()
print('GO Term Results by Ontology (DOM)\n')
for ns, (name, id_, count) in result.items():
    print(f"Ontology        : {ns}")
    print(f"Term Name       : {name}")
    print(f"Term ID         : {id_}")
    print(f"Number of is_a  : {count}")
end = datetime.now()
print(f"\nDOM time: {end - start}")


# XMLreading_SAX.py
import xml.sax
from datetime import datetime

class GOHandler(xml.sax.ContentHandler):
    def __init__(self):
        self.current_tag = ""
        self.name = ""
        self.id = ""
        self.namespace = ""
        self.isa_count = 0
        self.result = {
            "biological_process": ("", "", 0),
            "molecular_function": ("", "", 0),
            "cellular_component": ("", "", 0)
        }

    def startElement(self, tag, attrs):
        self.current_tag = tag
        if tag == "term":
            self.name = ""
            self.id = ""
            self.namespace = ""
            self.isa_count = 0
        elif tag == "is_a":
            self.isa_count += 1

    def endElement(self, tag):
        if tag == "term" and self.namespace in self.result:
            if self.isa_count > self.result[self.namespace][2]:
                self.result[self.namespace] = (self.name.strip(), self.id.strip(), self.isa_count)
        self.current_tag = ""

    def characters(self, content):
        if self.current_tag == "name":
            self.name += content
        elif self.current_tag == "id":
            self.id += content
        elif self.current_tag == "namespace":
            self.namespace += content

start = datetime.now()
parser = xml.sax.make_parser()
parser.setFeature(xml.sax.handler.feature_namespaces, 0)
handler = GOHandler()
parser.setContentHandler(handler)

try:
    parser.parse("go_obo.xml")
except Exception as e:
    print("Error during parsing:", e)
    exit()
print("GO Term Results by Ontology (SAX)\n")
for ns, (name, id_, count) in handler.result.items():
    print(f"Ontology        : {ns}")
    print(f"Term Name       : {name}")
    print(f"Term ID         : {id_}")
    print(f"Number of is_a  : {count}")

end = datetime.now()
print(f"\nSAX time: {end - start}")


#SAX way is faster than DOM way

