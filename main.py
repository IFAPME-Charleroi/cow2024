import asyncio
import subprocess

async def run_crowded_situation():
    # Exécuter le script crowded_situation.py
    print("Lancement de crowded_situation.py")
    process = await asyncio.create_subprocess_exec(
        'python', './utils_prod/crowded_situation.py',
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE
    )

    await process.communicate()

async def run_detective_mode():
    # Exécuter le script detective_mode.py
    print("Lancement de detective_mode.py")
    process = await asyncio.create_subprocess_exec(
        'python', './utils_prod/detective_mode.py',
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE
    )
    await process.communicate()

async def main():
    # Lancer crowded_situation.py en continu
    while True:
        await run_crowded_situation()

        # Attendre que l'utilisateur appuie sur la touche 'a' pour lancer le mode détective
        user_input = input("Appuyez sur 'a' pour lancer le mode détective: ")
        if user_input.lower() == 'a':
            # Lancer le mode détective
            await run_detective_mode()

# Exécuter la boucle principale asyncio
try:
    asyncio.run(main())
except KeyboardInterrupt:
    print("Arrêt de l'exécution.")
