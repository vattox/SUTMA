from django.shortcuts import render

def home(request):
    return render(request, 'core/home.html')

def contact(request):
    return render(request, 'core/contact.html')

def services(request):
    services_list = [
        {
            'id': 'btp',
            'title': 'Location Engins BTP',
            'short_desc': 'Terrassement, Niveleuses, Compacteurs',
            'full_desc': """
                <p><strong>SUTMA, votre partenaire de confiance pour la location d'engins BTP au Maroc.</strong></p>
                <p>Nous mettons à votre disposition une large gamme d'engins performants :</p>
                <ul>
                    <li>Pelles hydrauliques sur chenilles et sur pneus</li>
                    <li>Bulldozers & Chargeurs</li>
                    <li>Niveleuses & Compacteurs</li>
                    <li>Camions bennes & Tracteurs routiers</li>
                </ul>
                <p>Un parc matériel régulièrement renouvelé pour une productivité optimale.</p>
            """,
            'image': 'https://tp-amenagements.fr/wp-btp-2019/wp-content/uploads/2025/03/Next-Generation-New-Model-Teaser.png'
        },
        {
            'id': 'manutention',
            'title': 'Engins de Manutention',
            'short_desc': 'Chariots, Nacelles, Grues',
            'full_desc': """
                <p><strong>Solutions de levage et manutention pour tous vos besoins.</strong></p>
                <ul>
                    <li>Chariots élévateurs thermiques et électriques</li>
                    <li>Chariots télescopiques</li>
                    <li>Nacelles élévatrices toutes hauteurs</li>
                    <li>Grues mobiles</li>
                </ul>
                <p>Sécurité et performance garanties pour vos opérations logistiques.</p>
            """,
            'image': 'https://s7d2.scene7.com/is/image/Caterpillar/CM20241216-f1705-f1d42?$highres$'
        },
        {
            'id': 'divers',
            'title': 'Travaux Divers BTP',
            'short_desc': 'Construction, Voiries, Assainissement',
            'full_desc': """
                <p><strong>Expertise globale en construction et aménagements.</strong></p>
                <ul>
                    <li>Travaux de construction générale</li>
                    <li>Voiries et Réseaux Divers (VRD)</li>
                    <li>Assainissement et Adduction d'eau</li>
                    <li>Aménagements extérieurs</li>
                </ul>
            """,
            'image': 'https://images.unsplash.com/photo-1504307651254-35680f356dfd?w=1200&h=800&fit=crop&q=80'
        },
        {
            'id': 'event',
            'title': 'Infrastructure Événementielle',
            'short_desc': 'Chapiteaux, Scènes, Barrières',
            'full_desc': """
                <p><strong>Support logistique pour vos événements de grande envergure.</strong></p>
                <ul>
                    <li>Installation de structures temporaires</li>
                    <li>Barrières de sécurité & Palissades</li>
                    <li>Aménagement de zones VIP</li>
                    <li>Logistique technique</li>
                </ul>
            """,
            'image': 'https://images.unsplash.com/photo-1492684223066-81342ee5ff30?w=1200&h=800&fit=crop&q=80'
        },
        {
            'id': 'bureaux',
            'title': 'Bureaux & Toilettes Chantier',
            'short_desc': 'Modulaires, Sanitaires, Base de vie',
            'full_desc': """
                <p><strong>Installations de chantier confortables et conformes.</strong></p>
                <ul>
                    <li>Bureaux modulaires équipés</li>
                    <li>Blocs sanitaires mobiles</li>
                    <li>Réfectoires et Vestiaires</li>
                    <li>Bases de vie complètes</li>
                </ul>
            """,
            'image': 'https://instanttoilets.com.au/wp-content/uploads/2023/10/20230918_113534812_iOS-scaled.jpg'
        },
        {
            'id': 'groupes',
            'title': 'Groupes Électrogènes',
            'short_desc': 'Énergie mobile, Maintenance',
            'full_desc': """
                <p><strong>Énergie fiable où que vous soyez.</strong></p>
                <ul>
                    <li>Location de groupes électrogènes toutes puissances</li>
                    <li>Solutions d'alimentation temporaire</li>
                    <li>Maintenance et assistance technique 24/7</li>
                </ul>
            """,
            'image': 'https://www.whisperpower.com/content/uploads/2021/05/Generator_header_test.png'
        }
    ]
    return render(request, 'core/services.html', {'services': services_list})

def gallery(request):
    # List of all gallery images
    gallery_images = [
        {'src': 'core/images/6350fbd3bb61cef8c8aef9cd26f67bc8_1080x718_fit.JPG', 'title': 'Projet Infrastructure'},
        {'src': 'core/images/cd0df0cce139d68392d3b89ae1695123_1386x1040_fit.JPG', 'title': 'Chantier BTP'},
        {'src': 'core/images/d9b7fd67f2c9b572574b263f42fadaa7_1080x810_fit.jpg', 'title': 'Équipement Lourd'},
        {'src': 'core/images/d82b103c796deaab07992f4128b061a1_1080x608_fit.jpg', 'title': 'Construction'},
        {'src': 'core/images/b949681105456d4f43ac99c21183f324_1080x608_fit.jpg', 'title': 'Aménagement'},
        {'src': 'core/images/05e116235e96c064400aebf4c3be82cc_1080x1624_fit.JPG', 'title': 'Infrastructure'},
        {'src': 'core/images/nacelles.jpeg', 'title': 'Nacelles Élévatrices'},
        {'src': 'core/images/nac4.jpeg', 'title': 'Manutention'},
        {'src': 'core/images/nac5.jpeg', 'title': 'Engins de Levage'},
        {'src': 'core/images/512cede65aef3abf63d7a4086ecb5a4e_fit.jpg', 'title': 'Événementiel'},
        {'src': 'core/images/cbeton.jpeg', 'title': 'Béton & Matériaux'},
        {'src': 'core/images/usin4.jpeg', 'title': 'Usine & Production'},
        {'src': 'core/images/a6eb6d3b9ed3609598dc89f200d47e04_792x594_fit.jpg', 'title': 'Engins BTP'},
        {'src': 'core/images/752c7ba151942fbd0b056685b2534fbd_792x594_fit.jpg', 'title': 'Groupes Électrogènes'},
        {'src': 'core/images/cfce51540593fe3f2895d6f23d05ce4f_792x594_fit.jpeg', 'title': 'Bureaux Chantier'},
        {'src': 'core/images/f773468ef6c44be0f8c9750c30c2c7a4_fit.jpeg', 'title': 'Génie Civil'},
    ]
    return render(request, 'core/gallery.html', {'images': gallery_images})
