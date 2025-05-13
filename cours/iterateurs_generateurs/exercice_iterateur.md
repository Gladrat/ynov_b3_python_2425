# Exercice : Création d’un itérateur de numéros de facture

## 🎯 Objectif :

Créer une classe Python capable de générer automatiquement des numéros de facture **uniques** au format `FAC-001`, `FAC-002`, `FAC-003`, etc.

## 📌 Contraintes :

1. La classe s’appellera `InvoiceNumberIterator`.
2. Elle devra implémenter le protocole des itérateurs (`__iter__()` et `__next__()`).
3. Le numéro devra :
   - avoir un **préfixe configurable** (par défaut `"FAC"`)
   - être **paddé à 3 chiffres** (001, 002, …)
   - commencer à un **numéro de départ configurable** (par défaut `1`)

## ✅ Exemple attendu :

```python
invoices = InvoiceNumberIterator()

print(next(invoices))  # FAC-001
print(next(invoices))  # FAC-002

custom = InvoiceNumberIterator(prefix="INV", start=42)
print(next(custom))    # INV-042
print(next(custom))    # INV-043
```

## Astuce :

- Utiliser `f"{valeur:03}"` pour formatter les nombres à 3 chiffres.
- Ne pas oublier pas que `__iter__()` doit retourner `self`.