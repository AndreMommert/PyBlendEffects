#!/usr/bin/python
# -*- coding: utf-8 -*-

"""ESA 3 in Objektorientierte Skriptspachen
   Die Technologie mit der wir uns im Semesterabschlussprojekt beschäftigen wird Blender sein.
   Es soll eine Automatisierung von Blender mit Hilfe von Python erfolgen. Dadurch soll auch dem
   Laien ermöglich werden, Schrift-Effekte zu generieren, die dann als fertiges Video gerendet werden.
   Diese kurzen Videos können dann beispielsweise direkt auf eine Webseite eingebunden, oder
   als Vorspann vor ein eigentliches Video gelegt werden.

Usage:
  pyblendeffects.py effect (dissolve|glossy) <text>
"""

__author__ = 'reinschs@fh-brandenburg.de | patrick.walther.1989@gmx.de | mommert@fh-brandenburg.de'

import bpy
import sys
from HtmlRenderer import HtmlRenderer



def screenShot(count, title, description):
	bpy.ops.wm.redraw_timer(type='DRAW_WIN_SWAP', iterations=1)
	bpy.ops.screen.screenshot(filepath='D:/tmpImage/' + str(count) + '.png')
	html_renderer.add_step('D:/tmpImage/' + str(count) + '.png', title, description)

# Funktion für den Dissolve-Effekt
def DissolveEffect(text):
	print('DissolveEffect')
	count = 1
	
	bpy.ops.object.select_all(action='TOGGLE')
	bpy.ops.object.select_all(action='TOGGLE')
	
	screenShot(count, "Alle Elemente markieren und löschen", "Um alle Elemente zu selektieren, drück man die A-Taste. Sollte nun nichts selektiert werden, wird beim ersten Mal ein Element selektiert gewesen sein und man muss erneut die A-Taste drücken. Anschließend drück man X oder DEL auf seiner Tastatur und bestätigt das Löschen aller ausgewählten Elemente.")
	count += 1
	
	bpy.ops.object.delete(use_global=False)
	bpy.ops.mesh.primitive_cube_add(radius=1, view_align=False, enter_editmode=False, location=(0, 0, 0), rotation=(0, 0, 0), layers=(True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False))
	
	screenShot(count, "Einfach Cube hinzufügen", "Nachdem alle Elemente gelöscht wurden, muss ein einfach Cube hinzugefügt werden. Hierfür kann man die Tastenkombination Shift + A (alternativ über Add -> Mesh -> Cube) nutzen und dann unter Mesh -> Cube auswählen.")
	count += 1
	
	bpy.context.scene.render.engine = 'CYCLES'
	
	screenShot(count, "Ändern des Renderers", "Oben in der Menu-Leiste muss von Blender Render auf Cycles Render umgestellt werden")
	count += 1
	
	bpy.context.window.screen.areas[1].spaces[0].context = 'RENDER'
	bpy.context.scene.frame_end = 135
	
	screenShot(count, "Länge der Animation festlegen", "Unter den Einstellungen Render im Menu Properties kann der Start- und End-Frame gesetzt werden. Für diese Animation wird der End-Frame auf 135 gesetzt.")
	count += 1
	
	bpy.context.window.screen.areas[1].spaces[0].context = 'MATERIAL'
	mat_name = "defaultMaterial"
	bpy.data.materials.new(mat_name)
	bpy.data.materials[mat_name].use_nodes = True
	bpy.data.materials[mat_name].node_tree.nodes['Diffuse BSDF'].inputs['Color'].default_value = (0.8, 0.719635, 0, 1)
	in_1 = bpy.data.materials[mat_name].node_tree.nodes["Material Output"].inputs["Surface"]
	out_1 = bpy.data.materials[mat_name].node_tree.nodes["Diffuse BSDF"].outputs["BSDF"]
	bpy.data.materials[mat_name].node_tree.links.new(in_1, out_1)
	bpy.data.objects["Cube"].active_material = bpy.data.materials[mat_name]
	
	screenShot(count, "Material hinzufügen", "Nun wird es Zeit dem Cube ein Material hinzuzufügen. Dafür wählt man im rechten Bereich bei den Properties das Material aus (Symbol kleiner Ball). Man drück zuerst auf Use Nodes und gibt dem Material einen Namen und eine Farbe.")
	count += 1
	
	bpy.ops.object.move_to_layer(layers=(False, True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False))
	
	screenShot(count, "Cube auf einen anderen Layer verschieben", "Durch das Drücken der M-Taste erscheint ein Menu, welches eine Auswahl der vorhandenen Layer bietet. Durch drücken der Zahlen 0-9 bzw. Alt + 0-9 wird der aktive Cube auf den Layer 1-10 bzw. 11-20. (Zu beachten ist das die Zahl 0 für den Layer 10 steht und Alt + 0 für Layer 20)")
	count += 1
	
	bpy.ops.object.text_add(view_align=False, enter_editmode=False, location=(0, 0, 0), rotation=(0, 0, 0), layers=(True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False))
	bpy.ops.transform.rotate(value=1.5708, axis=(1, 0, 0), constraint_axis=(True, False, False), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1, snap=False, snap_target='CLOSEST', snap_point=(0, 0, 0), snap_align=False, snap_normal=(0, 0, 0), release_confirm=False)
	
	screenShot(count, "Text hinzufügen", "Wie auch bei dem Cude einfach über Shift + A oder über das Add-Menu einen Text hinzufügen. Schließend noch die folgenden Tasten hintereinander drücken: R X 90 und mit Enter bestätigen. Das bewirkt das der Text sich um die X-Achse um 90° dreht.")
	count += 1
	
	bpy.ops.object.editmode_toggle()
	bpy.ops.font.delete(type='PREVIOUS_OR_SELECTION')
	bpy.ops.font.delete(type='PREVIOUS_OR_SELECTION')
	bpy.ops.font.delete(type='PREVIOUS_OR_SELECTION')
	bpy.ops.font.delete(type='PREVIOUS_OR_SELECTION')
	for c in text:
		bpy.ops.font.text_insert(text=c, accent=False)
	bpy.ops.object.editmode_toggle()
	
	screenShot(count, "Text bearbeiten", "Durch das drücken von TAB auf einem Objekt gelangt man in den Edit-Mode. Da es sich hier um einen Text handelt, kann man diesen mittels Backspace-Taste löschen und den Text seiner Wahl eingeben. Am Ende bestätigt man seine Eingabe mit erneutem drücken der TAB-Taste.")
	count += 1
	
	bpy.context.window.screen.areas[1].spaces[0].context = 'DATA'
	bpy.context.object.data.extrude = 0.05
	bpy.context.object.data.bevel_depth = 0.02
	bpy.context.object.data.bevel_resolution = 2
	
	screenShot(count, "Texteingenschaften ändern", "In diesem Schritt werden die einzelnen Eigenschaften des Textes geändert. Dafür geht man bei den Properties auf das Textsymbol und hat eine breite Palette an Eigenschaften vor sich. In diesem Beispiel wird der Exturde-Faktore auf 0.05, der Depth-Faktor auf 0.02 und der Resolution-Faktor auf 2 gesetzt.")
	count += 1
	
	bpy.context.window.screen.areas[1].spaces[0].context = 'MATERIAL'
	bpy.data.objects["Text"].active_material = bpy.data.materials[mat_name]
	
	screenShot(count, "Text ein Matrial geben", "Hier wird dem Text das gleiche Material gegeben wie dem Cube. Um das Material zu verlinken drück man links neben dem New auf das Material-Symbol und wählt das bereits existierende Material aus.")
	count += 1
	
	bpy.ops.object.convert(target='MESH', keep_original=False)
	
	screenShot(count, "Text in ein Mesh wandeln", "Durch die Tastenkombination Alt + C oder dem Menueintrag Object -> Convert to wählt man den Eintrag Mesh from Curve/Meta/Surf/Text aus und der Text wird in ein normales Polygonobjekt umgewandelt.")
	count += 1
	
	bpy.context.window.screen.areas[1].spaces[0].context = 'PARTICLES'
	bpy.ops.object.particle_system_add()
	bpy.data.particles["ParticleSettings"].frame_start = 20
	bpy.data.particles["ParticleSettings"].frame_end = 30
	bpy.data.particles["ParticleSettings"].lifetime = 100
	bpy.data.particles["ParticleSettings"].distribution = 'RAND'
	bpy.data.particles["ParticleSettings"].render_type = 'OBJECT'
	bpy.data.particles["ParticleSettings"].dupli_object = bpy.data.objects["Cube"]
	bpy.data.particles["ParticleSettings"].particle_size = 0.01
	bpy.data.particles["ParticleSettings"].effector_weights.gravity = 0
	bpy.data.particles["ParticleSettings"].normal_factor = 0
	
	screenShot(count, "Particle-System hinzufügen", "Als nächstes wird das Particle-System zu dem konvertierten Text hinzugefügt. Es ist nach der Umwandlung ein neuer Eintrag bei den Properties erschienen. Unter den 4-Sternchen Symbol wird das Particle-System durch add hinzugefügt und mit folgenden Einstellungen versehen. Start = 20, End = 30, Lifetime = 100, bei der Auswahl Jittered-Random-Grid wird Random ausgewählt, Normal = 0, bei der Auswahl None-Halo-Line-Path-Object-Grozup-Billnoar wird Object ausgewählt, Dupli Object = Cube, Size = 0.01 und Gravity = 0")
	count += 1
	
	bpy.ops.object.effector_add(type='TURBULENCE', view_align=False, enter_editmode=False, location=(0, 0, 0), rotation=(0, 0, 0), layers=(True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False))
	bpy.ops.transform.translate(value=(2.5, 0, 0), constraint_axis=(True, False, False), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1, snap=False, snap_target='CLOSEST', snap_point=(0, 0, 0), snap_align=False, snap_normal=(0, 0, 0), texture_space=False, release_confirm=False)
	
	screenShot(count, "Wind hinzufügen", "Über Shift + A oder dem Add-Menu wird hier ein Force-Field Turbulence hinzugefügt.")
	count += 1
	
	bpy.context.window.screen.areas[1].spaces[0].context = 'PHYSICS'
	bpy.context.object.field.strength = 2
	
	screenShot(count, "Wind Einstellungen", "Dem Force-Field wird in den Physics-Einstellung die Stärke 2 gegeben.")
	count += 1
	
	bpy.context.scene.objects.active = bpy.data.objects["Text"]
	bpy.data.objects["Field"].select = False
	bpy.data.objects["Text"].select = True
	
	screenShot(count, "Text selektieren", "Da die Animation auf den Text stattfindet muss dieser zunächst wieder selektiert werden.")
	count += 1
	
	bpy.context.window.screen.areas[1].spaces[0].context = 'PARTICLES'
	bpy.data.objects['Text'].particle_systems["ParticleSystem"].settings.keyframe_insert(data_path="use_render_emitter", frame=1.0)
	
	screenShot(count, "Animation erstellen Part 1", "Für die Animation geht man in das Particle-System des Textes. Dort fährt man mit der Maus über die Eigenschaft Emitter und drück die I-Taste.")
	count += 1
	
	bpy.context.scene.frame_current = 30
	bpy.data.objects['Text'].particle_systems["ParticleSystem"].settings.keyframe_insert(data_path="use_render_emitter", frame=30.0)
	
	screenShot(count, "Animation erstellen Part 2", "Als nächste stellt man unten die Timeline auf Frame 30 und geht erneut über die Emitter-Eigenschaft und drück I.")
	count += 1
	
	bpy.context.scene.frame_current = 31
	bpy.data.particles["ParticleSettings"].use_render_emitter = False
	bpy.data.objects['Text'].particle_systems["ParticleSystem"].settings.keyframe_insert(data_path="use_render_emitter", frame=31.0)
	
	screenShot(count, "Animation erstellen Part 3", "Ein Frame weiter (Frame 31) wird der Haken rausgenommen und wieder beim Drübergehen mit der Maus die I-Taste gedrückt.")
	count += 1
	
	bpy.context.scene.frame_current = 70
	bpy.data.objects['Text'].particle_systems["ParticleSystem"].settings.keyframe_insert(data_path="particle_size", frame=70.0)
	
	screenShot(count, "Animation erstellen Part 4", "Im Frame 70 wird die I-Taste über der Eigenschaft Size gedrückt")
	count += 1
	
	bpy.context.scene.frame_current = 130
	bpy.data.particles["ParticleSettings"].particle_size = 0.001
	bpy.data.objects['Text'].particle_systems["ParticleSystem"].settings.keyframe_insert(data_path="particle_size", frame=130.0)
	
	screenShot(count, "Animation erstellen Part 5", "Zuletzt wird im Frame 130 der Wert Size auf 0.001 gesetzt und wieder darüber die I-Taste gedrückt.")
	count += 1
	
	bpy.ops.mesh.primitive_plane_add(radius=1, view_align=False, enter_editmode=False, location=(0, 0, 0), rotation=(0, 0, 0), layers=(True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False))
	bpy.ops.transform.translate(value=(0, 0, -0.1), constraint_axis=(False, False, True), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1, snap=False, snap_target='CLOSEST', snap_point=(0, 0, 0), snap_align=False, snap_normal=(0, 0, 0), texture_space=False, release_confirm=False)
	bpy.ops.transform.resize(value=(100, 100, 100), constraint_axis=(False, False, False), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1, snap=False, snap_target='CLOSEST', snap_point=(0, 0, 0), snap_align=False, snap_normal=(0, 0, 0), texture_space=False, release_confirm=False)
	bpy.context.window.screen.areas[1].spaces[0].context = 'PHYSICS'
	bpy.ops.object.modifier_add(type='COLLISION')
	
	screenShot(count, "Untergrund erstellen", "Für den Untergrund wird eine einfach Plan über das Add-Menu oder Shift + A hinzugefügt. Diese wird dann ein kleines Stückchen unterhalb des Textes plaziert. Anschließend wird mit der S-Taste und der Zahl 100, die Plan um das 100-Fache skaliert.")
	count += 1
	
	bpy.ops.object.lamp_add(type='POINT', view_align=False, location=(0, 0, 0), rotation=(0, 0, 0), layers=(True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False))
	
	screenShot(count, "Licht hinzufügen", "Auch hier wird wieder ein Elemente via Add-Menu oder Shift + A der Szene hinzugefügt. In diesem Schritt handelt es sich um ein Point-Light.")
	count += 1
	
	bpy.ops.transform.translate(value=(0, 0, 5), constraint_axis=(False, False, True), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1, snap=False, snap_target='CLOSEST', snap_point=(0, 0, 0), snap_align=False, snap_normal=(0, 0, 0), texture_space=False, release_confirm=False)
	bpy.ops.transform.translate(value=(0, -5, 0), constraint_axis=(False, True, False), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1, snap=False, snap_target='CLOSEST', snap_point=(0, 0, 0), snap_align=False, snap_normal=(0, 0, 0), texture_space=False, release_confirm=False)
	bpy.ops.transform.translate(value=(-6, 0, 0), constraint_axis=(True, False, False), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1, snap=False, snap_target='CLOSEST', snap_point=(0, 0, 0), snap_align=False, snap_normal=(0, 0, 0), texture_space=False, release_confirm=False)
	bpy.context.window.screen.areas[1].spaces[0].context = 'DATA'
	bpy.context.object.data.shadow_soft_size = 3
	bpy.data.lamps['Point'].node_tree.nodes['Emission'].inputs['Strength'].default_value = 5000
	
	screenShot(count, "Lichteinstellungen", "Nachdem hinzufügen des Lichtes wird es in der Szene positioniert und die Stärke des Lichtes wird auf 5000 gesetzt.")
	count += 1

	bpy.ops.object.camera_add(view_align=True, enter_editmode=False, location=(0, 0, 0), rotation=(1.26972, 0.0140788, -0.375695), layers=(True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False))
	
	screenShot(count, "Kamera hinzufügen", "Wie auch bei den anderen Objekten kann über das Add-Menu oder Shift + A eine Kamera hinzugefügt werden.")
	count += 1
	
	bpy.data.objects["Camera"].rotation_euler.x = 1.26973
	bpy.data.objects["Camera"].rotation_euler.y = 0.0140848
	bpy.data.objects["Camera"].rotation_euler.z = -0.3757
	
	bpy.data.objects["Camera"].location.x = 0.19936
	bpy.data.objects["Camera"].location.y = -5.34897
	bpy.data.objects["Camera"].location.z = 1.81676

	screenShot(count, "Kamera in die richtige Position bringen", "Hier wird die Kamera an die entsprechende Stelle positioniert. Diese kann frei gewählt werden, nur sollte sie auf den Text gerichtet sein.")
	count += 1
	
	bpy.context.window.screen.areas[1].spaces[0].context = 'WORLD'
	bpy.context.scene.world.horizon_color = (0, 0, 0)
	bpy.context.window.screen.areas[1].spaces[0].context = 'PHYSICS'
	bpy.data.particles["ParticleSettings"].count = 20000
	bpy.context.window.screen.areas[1].spaces[0].context = 'RENDER'
	bpy.context.scene.cycles.samples = 50
	bpy.context.scene.render.filepath = "/tmp/"
	bpy.context.scene.render.image_settings.file_format = 'FFMPEG'
	bpy.context.scene.frame_current = 1
	
	screenShot(count, "Render Einstellungen", "Am Ende werden nun die Einstellungen für den Renderer hinterlegt. Diese können beliebig gewählt werden. Hier im Besipiel wird der Hintergrund bei den Properties mit der Weltkugel auf schwarz gesetzt. Die Anzahl der Partikel wird auf 20000 erhöht. Die Rendereinstellungen wir auf 50 Samples gesetzt. Das Zielformat für eine Animation ist MPEG.")
	count += 1

# Funktion für den Glossy-Effekt
def GlossyEffect(text):
    print('Glossy')

    bpy.ops.object.select_all(action='TOGGLE')
    bpy.ops.object.select_all(action='TOGGLE')
    bpy.ops.object.delete(use_global=False)
    bpy.ops.object.text_add(view_align=False, enter_editmode=False, location=(0, 0, 0), rotation=(0, 0, 0), layers=(True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False))
    bpy.ops.transform.rotate(value=1.5708, axis=(1, 0, 0), constraint_axis=(True, False, False), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1, snap=False, snap_target='CLOSEST', snap_point=(0, 0, 0), snap_align=False, snap_normal=(0, 0, 0), release_confirm=False)
    bpy.ops.object.editmode_toggle()
    bpy.ops.font.delete(type='PREVIOUS_OR_SELECTION')
    bpy.ops.font.delete(type='PREVIOUS_OR_SELECTION')
    bpy.ops.font.delete(type='PREVIOUS_OR_SELECTION')
    bpy.ops.font.delete(type='PREVIOUS_OR_SELECTION')
    for c in text:
        bpy.ops.font.text_insert(text=c, accent=False)
    bpy.ops.object.editmode_toggle()
    #bpy.context.space_data.context = 'DATA'
    bpy.context.window.screen.areas[1].spaces[0].context = 'DATA'
    bpy.context.object.data.extrude = 0.3
    bpy.context.object.data.extrude = 0.3
    bpy.context.object.data.bevel_depth = 0.03
    bpy.context.object.data.bevel_resolution = 3
    bpy.context.object.data.extrude = 0.2
    bpy.context.scene.render.engine = 'CYCLES'
    #bpy.context.space_data.context = 'MATERIAL'
    bpy.context.window.screen.areas[1].spaces[0].context = 'MATERIAL'
    matName = "objMaterial"
    bpy.data.materials.new(matName)
    bpy.data.materials[matName].use_nodes = True
    bpy.data.node_groups["Shader Nodetree"].nodes["Glossy BSDF"].inputs[0].default_value = (0.8, 0.419435, 0.0352662, 1)
    bpy.data.node_groups["Shader Nodetree"].nodes["Glossy BSDF"].inputs[0].default_value = (0.8, 0.419435, 0.0352662, 1)
    bpy.ops.object.camera_add(view_align=True, enter_editmode=False, location=(0, 0, 0), rotation=(1.10871, 0.0132652, 1.14827), layers=(True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False))
    bpy.ops.view3d.camera_to_view()
    bpy.ops.object.lamp_add(type='POINT', view_align=False, location=(0, 0, 0), rotation=(0, 0, 0), layers=(True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False))
    bpy.ops.transform.translate(value=(0, -2, -2), constraint_axis=(False, False, False), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1, snap=False, snap_target='CLOSEST', snap_point=(0, 0, 0), snap_align=False, snap_normal=(0, 0, 0), texture_space=False, release_confirm=False)
    bpy.context.object.data.shadow_soft_size = 1
    bpy.data.node_groups["Shader Nodetree"].nodes["Emission"].inputs[1].default_value = 5000
    #bpy.context.space_data.context = 'WORLD'
    bpy.context.window.screen.areas[1].spaces[0].context = 'WORLD'
    bpy.context.scene.world.horizon_color = (0, 0, 0)
    bpy.context.scene.world.horizon_color = (0, 0, 0)
    bpy.ops.transform.translate(value=(1.7, 0, 1), constraint_axis=(False, False, False), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1, snap=False, snap_target='CLOSEST', snap_point=(0, 0, 0), snap_align=False, snap_normal=(0, 0, 0), texture_space=False, release_confirm=False)
    #bpy.context.space_data.context = 'DATA'
    bpy.context.window.screen.areas[1].spaces[0].context = 'DATA'
    #bpy.context.space_data.context = 'MATERIAL'
    bpy.context.window.screen.areas[1].spaces[0].context = 'MATERIAL'
    bpy.data.node_groups["Shader Nodetree"].nodes["Glossy BSDF"].inputs[1].default_value = 0.3
    bpy.ops.transform.translate(value=(0, 0, -1), constraint_axis=(False, False, True), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1, snap=False, snap_target='CLOSEST', snap_point=(0, 0, 0), snap_align=False, snap_normal=(0, 0, 0), texture_space=False, release_confirm=False)
    #TODO SWITCH WINDOW
    bpy.context.scene.use_nodes = True
    bpy.ops.node.add_node(use_transform=True, type="CompositorNodeGlare", settings=[])
    bpy.ops.transform.translate(value=(-135.307, 343.551, 0), constraint_axis=(False, False, False), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1, snap=False, snap_target='CLOSEST', snap_point=(0, 0, 0), snap_align=False, snap_normal=(0, 0, 0), texture_space=False, release_confirm=False)



# Haupteinstiegspunk
if __name__ == "__main__":
	arguments = sys.argv
	text = arguments[5]
	html_renderer = HtmlRenderer()
	html_renderer.set_copy_path("D:/tutorial")
	html_renderer.set_text('Dieses Tutorial leitet dich Schritt für Schritt an um den Effekt in Blender zu erstellen.')
	
	# Welcher Effekt soll generiert werden
	if arguments[4] == "dissolve":
		DissolveEffect(text)
		html_renderer.set_title('Tutorial Dissolve Text')
	elif arguments[4] == "glossy":
		GlossyEffect(text)
		html_renderer.set_title('Tutorial Glossy Text')
	
	html_renderer.render_html()

