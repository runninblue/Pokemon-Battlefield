const chai = require('chai');
const chaiHttp = require('chai-http');
const app = require('../src/server');

const expect = chai.expect;
chai.use(chaiHttp);

describe('GET /', () => {
    it('Gets server context message', (done) => {
        chai.request(app)
        .get('/')
        .end((err, res) => {
            expect(err).to.be.null;
            expect(res).to.have.status(200);
            expect(res.text).to.include('Pokemon Battlefield');
            expect(res).to.have.header('content-type', 'text/html; charset=utf-8');
            done();
        });
    });
});

describe('POST /', () => {
    it('Retrieves pokemon details', (done) => {
        const requestData = {
            pokemon1 : 'pikachu',
            pokemon2 : 'raichu'
        };

        chai.request(app)
            .post('/')
            .send(requestData)
            .end((err, res) => {
                expect(err).to.be.null;
                expect(res).to.have.status(200);
                done();
            });
    });
    it('Fails to retrieve pokemon details', (done) => {
        const requestData = {
            pokemon1 : 'pikachu',
            pokemon2 : 'rai'
        };

        chai.request(app)
            .post('/')
            .send(requestData)
            .end((err, res) => {
                expect(err).to.be.null;
                expect(res).to.have.status(404);
                expect(res.text).to.include('Pokemon not found');
                done();
            });
    });
});

describe('POST /type', () => {
    it('Retrieves pokemon type information', (done) => {
        const requestData = {
            url : 'https://pokeapi.co/api/v2/type/5'
        };

        chai.request(app)
        .post('/type')
        .send(requestData)
        .end((err, res) => {
            expect(err).to.be.null;
            expect(res).to.have.status(200);
            expect(res.body).to.be.an('object');
            expect(res.body).to.have.property('double_damage_to');
            expect(res.body.double_damage_to).to.be.an('array');
            done();
        });
    });
    it('Fails to retrieve pokemon type information', (done) => {
        const requestData = {
            url : 'https://google.com'
        };

        chai.request(app)
        .post('/type')
        .send(requestData)
        .end((err, res) => {
            expect(err).to.be.null;
            expect(res).to.have.status(404);
            expect(res.text).to.include('Type not found');
            done();
        });
    });
});

describe('POST /move', () => {
    it('Retrieves pokemon move information', (done) => {
        const requestData = {
            url : 'https://pokeapi.co/api/v2/move/10'
        };

        chai.request(app)
        .post('/move')
        .send(requestData)
        .end((err, res) => {
            expect(err).to.be.null;
            expect(res).to.have.status(200);
            expect(res.body).to.be.an('object');
            expect(res.body).to.have.property('power');
            expect(res.body.power).to.be.a('number');
            done();
        });
    });
    it('Fails to retrieve pokemon move information', (done) => {
        const requestData = {
            url : 'https://google.com'
        };

        chai.request(app)
        .post('/move')
        .send(requestData)
        .end((err, res) => {
            expect(err).to.be.null;
            expect(res).to.have.status(404);
            expect(res.text).to.include('Move not found');
            done();
        });
    });
});

describe('POST /ability', () => {
    it('Retrieves pokemon ability information', (done) => {
        const requestData = {
            url : 'https://pokeapi.co/api/v2/ability/100'
        };

        chai.request(app)
        .post('/ability')
        .send(requestData)
        .end((err, res) => {
            expect(err).to.be.null;
            expect(res).to.have.status(200);
            expect(res.body).to.be.an('object');
            expect(res.body).to.have.property('ability_desc');
            expect(res.body.ability_desc).to.be.a('string');
            done();
        });
    });
    it('Fails to retrieve pokemon ability information', (done) => {
        const requestData = {
            url : 'https://google.com'
        };

        chai.request(app)
        .post('/ability')
        .send(requestData)
        .end((err, res) => {
            expect(err).to.be.null;
            expect(res).to.have.status(404);
            expect(res.text).to.include('Ability not found');
            done();
        });
    });
});
