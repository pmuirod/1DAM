xquery version "3.0";

copy $liga := //liga
modify (
  for $equipo in //equipo
  return
  (
    rename node $equipo/integrantes as "plantilla",
    for $persona in //persona
    return
    (
     insert node attribute nombre {$persona/nombre} into $persona,
     delete node $persona/nombre,
     insert node element persona {$persona[@id = $equipo/plantilla/@jugadores]} into $equipo/plantilla,
     delete node $persona[@id = $equipo/plantilla/@jugadores]
    ),
    delete node $equipo/plantilla/@jugadores
  )
)
return
  $liga