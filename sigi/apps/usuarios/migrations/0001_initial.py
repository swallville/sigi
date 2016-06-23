# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-06-16 16:34
from __future__ import absolute_import
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name=u'CasaLegislativa',
            fields=[
                (u'id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name=u'ID')),
                (u'nome', models.CharField(max_length=100, verbose_name=u'Nome')),
                (u'sigla', models.CharField(max_length=100, verbose_name=u'Sigla')),
                (u'endereco', models.CharField(max_length=100, verbose_name=u'Endereço')),
                (u'cep', models.CharField(max_length=100, verbose_name=u'CEP')),
                (u'municipio', models.CharField(max_length=100, verbose_name=u'Município')),
                (u'uf', models.CharField(choices=[(u'AC', u'Acre'), (u'AL', u'Alagoas'), (u'AP', u'Amapá'), (u'AM', u'Amazonas'), (u'BA', u'Bahia'), (u'CE', u'Ceará'), (u'DF', u'Distrito Federal'), (u'ES', u'Espírito Santo'), (u'GO', u'Goiás'), (u'MA', u'Maranhão'), (u'MT', u'Mato Grosso'), (u'MS', u'Mato Grosso do Sul'), (u'MG', u'Minas Gerais'), (u'PR', u'Paraná'), (u'PB', u'Paraíba'), (u'PA', u'Pará'), (u'PE', u'Pernambuco'), (u'PI', u'Piauí'), (u'RJ', u'Rio de Janeiro'), (u'RN', u'Rio Grande do Norte'), (u'RS', u'Rio Grande do Sul'), (u'RO', u'Rondônia'), (u'RR', u'Roraima'), (u'SC', u'Santa Catarina'), (u'SE', u'Sergipe'), (u'SP', u'São Paulo'), (u'TO', u'Tocantins'), (u'EX', u'Exterior')], max_length=100, verbose_name=u'UF')),
                (u'telefone', models.CharField(blank=True, max_length=100, verbose_name=u'Telefone')),
                (u'endereco_web', models.URLField(blank=True, max_length=100, verbose_name=u'HomePage')),
                (u'email', models.EmailField(blank=True, max_length=100, verbose_name=u'E-mail')),
            ],
            options={
                u'verbose_name': u'Casa Legislativa',
                u'verbose_name_plural': u'Casas Legislativas',
            },
        ),
        migrations.CreateModel(
            name=u'Subsecretaria',
            fields=[
                (u'id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name=u'ID')),
                (u'nome', models.CharField(max_length=100, null=True, verbose_name=u'Nome')),
                (u'sigla', models.CharField(max_length=10, null=True, verbose_name=u'Sigla')),
            ],
            options={
                u'verbose_name': u'Subsecretaria',
                u'ordering': (u'nome', u'sigla'),
                u'verbose_name_plural': u'Subsecretarias',
            },
        ),
        migrations.CreateModel(
            name=u'Telefone',
            fields=[
                (u'id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name=u'ID')),
                (u'tipo', models.CharField(choices=[(u'FIXO', u'FIXO'), (u'CELULAR', u'CELULAR')], max_length=7, verbose_name=u'Tipo Telefone')),
                (u'ddd', models.CharField(max_length=2, verbose_name=u'DDD')),
                (u'numero', models.CharField(max_length=10, verbose_name=u'Número')),
                (u'principal', models.CharField(choices=[(None, u'----'), (False, u'Não'), (True, u'Sim')], max_length=10, verbose_name=u'Telefone Principal?')),
            ],
            options={
                u'verbose_name': u'Telefone',
                u'verbose_name_plural': u'Telefones',
            },
        ),
        migrations.CreateModel(
            name=u'Usuario',
            fields=[
                (u'id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name=u'ID')),
                (u'username', models.CharField(max_length=50, unique=True, verbose_name=u'Nome de Usuário')),
                (u'nome_completo', models.CharField(max_length=128, verbose_name=u'Nome Completo')),
                (u'data_criacao', models.DateTimeField(default=django.utils.timezone.now, verbose_name=u'Data Criação')),
                (u'data_ultima_atualizacao', models.DateTimeField(default=django.utils.timezone.now, verbose_name=u'Última atualização')),
                (u'email', models.EmailField(max_length=254, unique=True, verbose_name=u'Email')),
                (u'habilitado', models.BooleanField(default=False, verbose_name=u'Habilitado?')),
                (u'conveniado', models.BooleanField(default=False)),
                (u'responsavel', models.BooleanField(default=False)),
                (u'rg', models.CharField(max_length=9, null=True, verbose_name=u'RG')),
                (u'cpf', models.CharField(default=u'00000000000', max_length=11, verbose_name=u'CPF')),
                (u'cargo', models.CharField(default=u'--------', max_length=30, verbose_name=u'Cargo')),
                (u'vinculo', models.CharField(choices=[(u'Tercerizado', u'Tercerizado'), (u'Efetivo', u'Efetivo'), (u'Contratado', u'Contratado')], default=u'--------', max_length=30, verbose_name=u'Vinculo')),
                (u'casa_legislativa', models.CharField(default=u'--------', max_length=30, verbose_name=u'Casa Legislativa')),
                (u'primeiro_telefone', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name=u'primeiro_telefone', to=u'usuarios.Telefone')),
                (u'segundo_telefone', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name=u'segundo_telefone', to=u'usuarios.Telefone')),
                (u'user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                u'verbose_name': u'Usuário',
                u'verbose_name_plural': u'Usuários',
            },
        ),
    ]