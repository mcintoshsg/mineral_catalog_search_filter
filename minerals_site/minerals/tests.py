''' unitests for our apps model, views, forms and templatetags.
'''
from django.urls import reverse
from django.test import TestCase

from .models import Mineral

mineral_data_1 = {
    "name": "Abelsonite",
    "img_filename": "240px-Abelsonite_-_Green_River_Formation%2C_Uintah_County%2C_Utah%2C_USA.jpg",
    "img_caption": "Abelsonite from the Green River Formation, Uintah County, Utah, US",
    "category": "Organic",
    "formula": "C<sub>31</sub>H<sub>32</sub>N<sub>4</sub>Ni",
    "strunz_classification": "10.CA.20",
    "crystal_system": "Triclinic",
    "unit_cell": "a = 8.508 Å, b = 11.185 Åc=7.299 Å, α = 90.85°β = 114.1°, γ = 79.99°Z = 1",
    "color": "Pink-purple, dark greyish purple, pale purplish red, reddish brown",
    "crystal_symmetry": "Space group: P1 or P1Point group: 1 or 1",
    "cleavage": "Probable on {111}",
    "mohs_hardness": "2–3",
    "luster": "Adamantine, sub-metallic",
    "streak": "Pink",
    "diaphaneity": "Semitransparent",
    "optical_properties": "Biaxial",
    "refractive_index": "",
    "group": "Organic Minerals"
    }

mineral_data_2 = {
    "name": "Abernathyite",
    "img_filename": "240px-Abernathyite%2C_Heinrichite-497484.jpg",
    "img_caption": "Pale yellow abernathyite crystals and green heinrichite crystals",
    "category": "Arsenate",
    "formula": "K(UO<sub>2</sub>)(AsO<sub>4</sub>)·<sub>3</sub>H<sub>2</sub>O",
    "strunz_classification": "08.EB.15",
    "crystal_system": "Tetragonal",
    "unit_cell": "a = 7.176Å, c = 18.126ÅZ = 4",
    "color": "Yellow",
    "crystal_symmetry": "H-M group: 4/m 2/m 2/mSpace group: P4/ncc",
    "cleavage": "Perfect on {001}",
    "mohs_hardness": "2.5–3",
    "luster": "Sub-Vitreous, resinous, waxy, greasy",
    "streak": "Pale yellow",
    "diaphaneity": "Transparent",
    "optical_properties": "Uniaxial (-)",
    "refractive_index": "nω = 1.597 – 1.608nε = 1.570",
    "group": "Arsenates"
    }


# test the model
class MineralModelTests(TestCase):
    ''' testing of the mineral model '''
    def setUp(self):
        ''' setup up dummy data in our model '''
        self.mineral_1 = Mineral.objects.create(**mineral_data_1)
        self.mineral_2 = Mineral.objects.create(**mineral_data_2)

    def test_mineral_creation(self):
        ''' test out the creation of our model '''
        mineral = Mineral.objects.get(name="Abelsonite")
        self.assertEqual(mineral, self.mineral_1)
        mineral = Mineral.objects.get(name="Abernathyite")
        self.assertEqual(mineral, self.mineral_2)


# test the views
class MineralViewsTest(TestCase):
    ''' testing the list and detail minerals views '''
    def setUp(self):
        self.mineral = Mineral.objects.create(**mineral_data_1)

    def test_mineral_detail_view(self):
        response = self.client.get(reverse('minerals:detail',
                                   kwargs={'pk': self.mineral.pk}))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(self.mineral, response.context['mineral'])
        self.assertTemplateUsed(response, 'minerals/detail.html')
        self.assertContains(response, self.mineral.name)

    def test_mineral_list_by_letter_view(self):
        ''' tests:
            1. test the page loads with the correct minerals by letter
        '''
        test = '<a class="minerals__anchor" href="/minerals/1/">Abelsonite</a>'
        response = self.client.get(reverse('minerals:letter_filter',
                                   kwargs={'letter': 'A'}))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'minerals/index.html')
        self.assertContains(response, test)

    def test_mineral_list_by_letter__fail_view(self):
        ''' tests:
            1. test a letter with no response informs user
        '''
        response = self.client.get(reverse('minerals:letter_filter',
                                   kwargs={'letter': 'Q'}))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'minerals/index.html')
        self.assertContains(response, 'Minerals matching query do not exist!')   

    def test_mineral_group_filter_view(self):
        ''' tests:
            1. test that the page loads with the correct group
        '''
        test = '<h3 class="text-centered">Mineral Group : Oxides</h3>'
        response = self.client.get(reverse('minerals:group_filter',
                                   kwargs={'group': 'Oxides'}))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'minerals/index.html')
        self.assertContains(response, test)

    def test_mineral_search_pass_view(self):
        ''' tests
            1. Test for a good responseonse - i.e Mineral exists
        '''
        search = "Abelsonite"
        test = '<h1 class="mineral__name">Abelsonite</h1>'

        response = self.client.post('/minerals/', {'search_query': search})
        self.assertTemplateUsed(response, 'minerals/detail.html')
        self.assertContains(response, test)

    def test_mineral_search_fail_view(self):
        ''' tests
            1. Test for a bad response - i.e Mineral does not exists
        '''
        search = "Aaskjdhaj"
        test = 'Mineral matching search does not exist!'

        response = self.client.post('/minerals/', {'search_query': search})
        self.assertRedirects(response, '/minerals/A',
                             fetch_redirect_response=False
                             )
        response = self.client.get('/minerals/A')                     
        self.assertContains(response, test)

