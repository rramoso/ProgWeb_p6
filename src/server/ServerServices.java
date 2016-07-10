package server;

import javax.jws.WebMethod;
import javax.jws.WebService;
import javax.xml.ws.Endpoint;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

/**
 * Created by ricardoramos on 7/7/16.
 */

@WebService()
public class ServerServices {

    static Map<String, Estudiante> studentsMap = new HashMap<>();
    static List<Asignatura> subjects = new ArrayList<>();

    @WebMethod
    public void crearEstudiante(int id, String name, String career, List<Asignatura> studentSubjects) {
        Estudiante newStudent = new Estudiante(id, name, career);
        newStudent.setSubjects(studentSubjects);
        String stringId = String.valueOf(id);
        studentsMap.put(stringId, newStudent);
    }

    @WebMethod
    public Asignatura getAsignatura(int index) {
        return subjects.get(index);
    }

    @WebMethod
    public List<Asignatura> listAsignatura() {
        return subjects;
    }

    @WebMethod
    public Estudiante getEstudiante(int id) {
        String stringId = String.valueOf(id);
        return studentsMap.get(stringId);
    }

    @WebMethod
    public void updateEstudiante(Estudiante student) {
        String stringId = String.valueOf(student.getId());
        studentsMap.put(stringId, student);
    }

    @WebMethod
    public void removeEstudiante(int id) {
        String stringId = String.valueOf(id);
        studentsMap.remove(stringId);
    }

    @WebMethod
    public List<Estudiante> listEstudiantes() {
        return new ArrayList<Estudiante>(studentsMap.values());
    }

    private static void createSubjects() {

        subjects.add(new Asignatura("ISC-436", "Aseguramiento Calidad del Software"));
        subjects.add(new Asignatura("ILE-498", "Ingles para Ingenieros"));
        subjects.add(new Asignatura("ISC-317", "Programacion Logica"));
        subjects.add(new Asignatura("ISC-446", "Mineria de Datos"));
        subjects.add(new Asignatura("ITT-325", "Redes de datos II"));

    }

    public static void main(String[] argv) {
        createSubjects();
        Object implementor = new ServerServices();
        String address = "http://localhost:8080/ServerService";
        Endpoint.publish(address, implementor);
    }
}
