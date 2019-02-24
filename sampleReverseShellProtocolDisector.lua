protocolo_shellInverso = Proto("ShellInv",  "Nuestro Protocolo de shell inverso")

campo_numerico= ProtoField.int32 ("mongodb.number_to_return", "numberToReturn"    , base.DEC)
campo_texto           = ProtoField.string("mongodb.query"           , "query"             , base.ASCII)

protocolo_shellInverso.fields = {campo_numerico,campo_texto}

function protocolo_shellInverso
.dissector(buffer, pinfo, tree)
  length = buffer:len()
  if length == 0 then return end

  pinfo.cols.protocol = protocolo_shellInverso
 .name

  local subtree = tree:add(protocolo_shellInverso, buffer(), "Data del ShellInv")
  local mensaje_descriptivo = "Este es un mensaje adicional"
  subtree:add(campo_texto, buffer(0,2)):append_text(" (" .. mensaje_descriptivo .. ")")
  subtree:add(campo_numerico, buffer(0,1)):append_text(" (" .. "Mi campo numerico" .. ")")
end

local tcp_port = DissectorTable.get("tcp.port")
tcp_port:add(2222, protocolo_shellInverso)