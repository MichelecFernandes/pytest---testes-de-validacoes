from src.service.service_user import ServiceUser

class TestServiceUser:

    # def test_add_user_success(self):
    #     name_add = 'Leonardo'
    #     job_add = 'TechLead'
    #     result_expect = 'Usuario adicionado com sucesso'
    #     service = ServiceUser()
    #     result = service.add_user(name=name_add, job=job_add)
    #     assert result_expect == result

    # def test_add_user_exits(self):
    #     name_exits = 'Thiago'
    #     job_exits = 'Tester'
    #     result_expect = 'Usuario ja cadastrado'
    #     service = ServiceUser()
    #     result = service.add_user(name=name_exits, job=job_exits)
    #     assert result_expect == result

    # def test_add_user_fail(self):
    #     name_fail = None
    #     job_fail = None
    #     result_expect = 'Usuario nao adicionado'
    #     service = ServiceUser()
    #     result = service.add_user(name=name_fail, job=job_fail)
    #     assert result_expect == result

    # def test_add_user_without_name_or_job(self):
    #     name_null = 123
    #     job_null = 458
    #     result_expect = 'Nome ou Profissão precisa ser um texto'
    #     service = ServiceUser()
    #     result = service.add_user(name=name_null, job=job_null)
    #     assert result_expect == result


    # def test_validate_null_job(self):
    #     name_null = 'Matheus'
    #     job_null = None
    #     result_expect = 'Usuario nao adicionado'
    #     service = ServiceUser()
    #     result = service.add_user(name=name_null, job=job_null)
    #     assert result_expect == result
    
    
    # def test_user_update(self):
    #     name_update = 'Carlos'
    #     job_update = 'Carpinteiro'
    #     result_expect = 'Profissão atualizada com sucesso'
    #     service = ServiceUser()
    #     result = service.update_user(name=name_update, new_job=job_update)
    #     assert result_expect == result
    

    def test_user_update_not_found(self):
        name_update = 'Flora'
        job_update = 'Carpinteiro'
        result_expect = 'Usuario não encontrado'
        service = ServiceUser()
        result = service.update_user(name=name_update, new_job=job_update)
        assert result_expect == result










    # def test_del_user(self):
    #     name_del = 'Ana'
    #     result_expect = 'Usuario removido'
    #     service = ServiceUser()
    #     result = service.del_user(name=name_del)
    #     assert result_expect == result
    
    
    # def test_select_user(self):
    #     name_select = 'Ricardo'
    #     result_expect = 'Profissão: Cibersegurança'
    #     service = ServiceUser()
    #     result = service.select_user(name=name_select)
    #     assert result_expect == result